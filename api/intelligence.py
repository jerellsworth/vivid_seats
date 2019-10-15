class BestPurchaseModel():
    def __init__(self, db):
        self.db = db

    def get_best_ticket(event_id):
        # TODO better algorithm
        tickets = self.db.get_tickets(event_id)
        return min(tickets, key=lambda t: t['price_each'])
