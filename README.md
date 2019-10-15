# vivid_seats

## Model

### web_site_events
* ws_event_id
* ws_event_type (search, purchase, etc.)
* referral_id
* purchase_id (null if not a purchase event)
* customer_id
* created_at

### purchases

* purchase_id
* customer_id
* ticket_id
* seller_id
* qty

### tickets

* ticket_id
* event_id
* section
* row
* qty

A ticket here actually represents some number of tickets in the same row.
Consequently, more than one purchase can map to the same ticket

### referrals

* referral_id
* referral_name

### events

* event_id
* event_name
* venue_id
* start_dt
* end_dt

### venues

* venue_id
* venue_address

### sellers

* seller_id
* seller_name

### customers

* customer_id
* customer_email
* customer_address
