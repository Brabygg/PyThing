-- SQLite
CREATE TABLE towers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    collapsed BOOLEAN NOT NULL,
    status TEXT
)