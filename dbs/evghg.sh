#! /bin/bash

dropdb EVGHG;
createdb EVGHG;

psql -U postgres -d EVGHG < /home/lion/dbs/ddl.sql
sh ./populate_table.sh


