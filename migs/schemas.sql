PRAGMA foreign_keys = ON;

CREATE TABLE web_site_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ws_event_type TEXT NOT NULL,
  referrer_id INTEGER,
  purchase_id INTEGER,
  customer_id INTEGER,
  created_at DATETIME NOT NULL,
  FOREIGN KEY(referrer_id) REFERENCES referrers(id),
  FOREIGN KEY(purchase_id) REFERENCES purchases(id),
  FOREIGN KEY(customer_id) REFERENCES customers(id)
);

CREATE TABLE purchases (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  ticket_id INTEGER NOT NULL,
  qty INTEGER NOT NULL,
  updated_at DATETIME NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customers(id),
  FOREIGN KEY(ticket_id) REFERENCES tickets(id)
);

CREATE TABLE tickets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id INTEGER NOT NULL,
  seller_id INTEGER NOT NULL,
  section TEXT,
  seat_row TEXT,
  qty INt8 NOT NULL,
  price_each NUMERIC,
  FOREIGN KEY(event_id) REFERENCES events(id),
  FOREIGN KEY(seller_id) REFERENCES sellers(id)
);

CREATE TABLE referrers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  referrer_name TEXT
);

CREATE TABLE events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  venue_id INTEGER,
  event_name TEXT,
  start_dt DATETIME,
  end_dt DATETIME,
  FOREIGN KEY(venue_id) REFERENCES venues(id)
);

CREATE TABLE venues (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  address TEXT
);

CREATE TABLE sellers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT
);

CREATE TABLE customers (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT,
  mailing_address TEXT
);
