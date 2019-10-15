# vivid_seats

## Setup

* Build and enter a python3 virtual environment
* `pip install -r requirements.txt`
* `python utils.py init`

## Running

* `python utils.py webserver`
* In another terminal session, enter the virtual environment and run
  `python utils.py tests` for a minimal test suite

## Model

### web_site_events
* id
* ws_event_type (search, purchase, etc.)
* referrer_id
* purchase_id (null if not a purchase event)
* customer_id
* created_at

### purchases

* id
* customer_id
* ticket_id
* qty

### tickets

* id
* event_id
* seller_id
* section
* row
* qty

A ticket here actually represents some number of tickets in the same row.
Consequently, more than one purchase can map to the same ticket

### referrers

* id
* referrer_name

### events

* id
* event_name
* venue_id
* start_dt
* end_dt

### venues

* id
* venue_address

### sellers

* id
* seller_name

### customers

* id
* customer_email
* customer_address
