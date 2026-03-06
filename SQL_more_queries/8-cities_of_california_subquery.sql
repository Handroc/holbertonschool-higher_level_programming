-- Lists all cities of California that can be found in the database hbtn_0e_4_usa.
SELECT state_id, name
FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC
