PRAGMA foreign_keys = ON;

CREATE TABLE web_site_events (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  ws_event_type TEXT NOT NULL,
  referrer_id INT8,
  purchase_id INT8,
  customer_id INT8,
  created_at DATETIME NOT NULL,
  FOREIGN KEY(referrer_id) REFERENCES referrer(id),
  FOREIGN KEY(purchase_id) REFERENCES purchases(id),
  FOREIGN KEY(customer_id) REFERENCES customer(id)
);

CREATE TABLE purchases (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  customer_id INT8 NOT NULL,
  ticket_id INT8 NOT NULL,
  qty INTEGER NOT NULL,
  updated_at DATETIME NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customer(id),
  FOREIGN KEY(ticket_id) REFERENCES ticket(id)
);

CREATE TABLE tickets (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  event_id INT8 NOT NULL,
  seller_id INT8 NOT NULL,
  section TEXT,
  row TEXT,
  qty INt8 NOT NULL,
  FOREIGN KEY(event_id) REFERENCES event(id),
  FOREIGN KEY(seller_id) REFERENCES seller(id)
);

CREATE TABLE referrers (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  referrer_name TEXT
);

CREATE TABLE EVENTS (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  venue_id INT8,
  event_name TEXT,
  start_dt DATETIME,
  end_dt DATETIME,
  FOREIGN KEY(venue_id) REFERENCES venues(id)
);

CREATE TABLE venues (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  address TEXT
);

CREATE TABLE sellers (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

CREATE TABLE customers (
  id INT8 PRIMARY KEY AUTOINCREMENT,
  email TEXT,
  mailing_address TEXT
);
