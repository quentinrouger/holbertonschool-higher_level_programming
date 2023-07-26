-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Query for task 8.
SELECT id, name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
