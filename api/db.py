import datetime as dt
import io
import sqlite3

class TicketsDB():
    # TODO this should use a real orm. Faking it for now
    def __init__(self, db_path):
        self.db_path = db_path

    def _get_conn(self):
        # we have to make a new conn for every request due to sqlite3 
        # allergy to multithreading
        return sqlite3.connect(self.db_path)

    def get_tickets(self, event_id):
        # TODO don't return sold tickets
        sql = ('SELECT id, section, seat_row, qty, price_each '
               'FROM tickets '
               'WHERE event_id = ?')
        curs = self._get_conn().cursor()
        curs.execute(sql, event_id)
        ret = []
        for r in curs:
            ret.append(dict(id=r[0],
                            section=r[1],
                            seat_row=r[2],
                            qty=r[3],
                            price_each=r[4]))
        curs.close()
        return ret

    def put_ticket(self, **kwargs):
        # TODO reconcile model with arguments
        cols = list(kwargs.keys()) + ['updated_at']
        vals = list(kwargs.values()) + [dt.datetime.now().isoformat()]
        sql = 'INSERT INTO tickets ({}) VALUES ({})'.format(
                ', '.join(('"{}"'.format(c) for c in cols)),
                ', '.join('?' * len(cols)))
        conn = self._get_conn()
        with conn:
            conn.execute(sql, vals)

    def purchase_ticket(self, customer_id, ticket_id, qty):
        sql_io = io.StringIO()
        sql_io.write('BEGIN\n\n')
        sql_io.write('INSERT INTO purchases (\n')
        sql_io.write('  customer_id, ticket_id, qty, updated_at)\n')
        sql_io.write('VALUES (?, ?, ?, ?);\n\n')
        sql_io.write('INSERT INTO web_site_events (\n')
        sql_io.write('  ws_event_type, purchase_id, customer_id, \n')
        sql_io.write('  created_at)\n')
        sql_io.write('SELECT \'PURCHASE\', MAX(id), ?, ?\n')
        sql_io.write('FROM purchases;\n')
        sql_io.write('COMMIT;\n')
        ts = dt.datetime.now().isoformat()
        conn = self._get_conn()
        with conn:
            conn.execute(
                sql_io.getvalue(),
                (customer_id, ticket_id, qty, ts, customer_id, ts))
