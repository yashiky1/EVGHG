#! /bin/bash

psql EVGHG -c "\copy electric_vehicles FROM '/home/lion/dbs/ev2.csv'
DELIMITER ',' 
CSV HEADER;
"
psql EVGHG -c "\copy Community_Prof FROM '/home/lion/dbs/cp.csv'
DELIMITER ',' 
CSV HEADER;
"

psql EVGHG -c "\copy GHG FROM '/home/lion/dbs/GHG.csv'
DELIMITER ',' 
CSV HEADER;
"

psql EVGHG -c "\copy Fuel_vehicles FROM '/home/lion/dbs/fv.csv'
DELIMITER ',' 
CSV HEADER;
"










