import os

import flask
import yaml

from .db import TicketsDB
from .intelligence import BestPurchaseModel

# TODO put this init code in a class rather than dumping it in global namespace
# Flask is notoriously resistant to OO style

LIB_PATH = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = os.path.join(LIB_PATH, '..')
CONF_PATH = os.path.join(REPO_PATH, 'conf.yml')

with open(CONF_PATH) as f_conf:
    conf = yaml.safe_load(f_conf)

db = TicketsDB(conf['db_path'])
best_purch_model = BestPurchaseModel(db)
app = flask.Flask(__name__)

# TODO depending on business needs, we'll want to reformat db output here
# TODO return values on put methods

@app.route('/events/<event_id>/tickets', methods=['GET'])
def get_event_tickets(event_id):
    return db.get_tickets(event_id)

@app.route('/tickets', methods=['POST'])
def post_ticket():
    # TODO indiscriminately throwing data into the db from http is bad.
    # We should be sanitizing and processing here
    db.put_ticket(**flask.request.get_json())

@app.route('/tickets/<ticket_id>/purchase', methods=['PUT'])
def put_ticket_purchase(ticket_id):
    data = flask.request.get_json()
    # TODO make sure that required data is present
    db.purchase_ticket(data['customer_id'], data['ticket_id'], data['qty'])

@app.route('/events/<event_id>/tickets/best', methods=['GET'])
def get_event_tickets_best(event_id):
    return best_purch_model.get_best_ticket(event_id)
