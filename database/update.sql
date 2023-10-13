-- SQLite
UPDATE towers
SET collapsed = FALSE,
    status = NULL
WHERE
    name = 'Burj Khalifa'