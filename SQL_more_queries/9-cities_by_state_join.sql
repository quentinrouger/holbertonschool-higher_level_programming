-- Script that lists all cities contained in the database hbtn_0d_usa.
-- Query for task 9.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON state_id = states.id
ORDER BY cities.id ASC;
