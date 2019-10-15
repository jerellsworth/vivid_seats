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

@app.route('/events/<event_id>/tickets', methods=['GET'])
def get_event_tickets(event_id):
    return flask.jsonify(db.get_tickets(event_id))

@app.route('/tickets', methods=['POST'])
def post_ticket():
    # TODO indiscriminately throwing data into the db from http is bad.
    # We should be sanitizing and processing here
    # TODO should return page for newly created ticket
    db.put_ticket(**flask.request.get_json())
    return ('', 201)

@app.route('/tickets/<ticket_id>/purchase', methods=['PUT'])
def put_ticket_purchase(ticket_id):
    # TODO should return altered ticket
    data = flask.request.get_json()
    # TODO make sure that required data is present
    db.purchase_ticket(data['customer_id'], ticket_id, data['qty'])
    return ('', 201)

@app.route('/events/<event_id>/tickets/best', methods=['GET'])
def get_event_tickets_best(event_id):
    return best_purch_model.get_best_ticket(event_id)
