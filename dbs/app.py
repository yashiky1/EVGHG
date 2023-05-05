#! /usr/bin/python3

"""
This is an example Flask | Python | Psycopg2 | PostgreSQL
application that connects to the 7dbs database from Chapter 2 of
_Seven Databases in Seven Weeks Second Edition_
by Luc Perkins with Eric Redmond and Jim R. Wilson.
The CSC 315 Virtual Machine is assumed.

John DeGood
degoodj@tcnj.edu
The College of New Jersey
Spring 2020

----

One-Time Installation

You must perform this one-time installation in the CSC 315 VM:

# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask

----

Usage

To run the Flask application, simply execute:

export FLASK_APP=app.py 
flask run
# then browse to http://127.0.0.1:5000/

----

References

Flask documentation:  
https://flask.palletsprojects.com/  

Psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    print(query)
    conn = None
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows
 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# handle venue POST and serve result web page
@app.route('/municipality-handler', methods=['POST'])
def municipality_handler():
    rows = connect('SELECT Total_personal_vehicles, NO_EVs, Percent_EVs FROM electric_vehicles WHERE MUNICIPALITY = ' + "'" + request.form['MUNICIPALITY'] + "'" + ';')
    heads = ['Total_personal_vehicles', 'NO_EVs', 'Percent_EVs'] 
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/EVownership-handler', methods=['POST'])
def EVownership_handler():
    rows = connect('SELECT Municipality, Percent_EVs FROM electric_vehicles WHERE Percent_EVs IS NOT NULL limit 4;')
    heads = ['Municipality', 'Percent EVs'] 
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/FVemissions-handler', methods=['POST'])
def FVemissions_handler():
    rows = connect('SELECT MUNICIPALITY, Fuel_vehicle_emissions FROM Fuel_Vehicles WHERE MUNICIPALITY IN (' + "'" + 'Pine Valley borough' + "'" + ', ' + "'" + 'Tavistock borough' + "'" + ', ' + "'" + 'Walpack township' + "'" + ', ' + "'" + 'Deal borough' + "'" + ');')
    heads = ['Municipality', 'Fuel Vehicle Emission'] 
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/FVJOINCP-handler', methods=['POST'])
def FVJOINCP_handler():
    rows = connect('SELECT * FROM Fuel_vehicles NATURAL JOIN Community_Prof;')
    heads = ['Municipality', 'County', 'Years', 'Passenger Cars', 'Total Miles Traveled', 'Fuel Vehicles Emissions', 'Square Miles', 'Population', 'Medium Household Income', 'Percent Pop. Poverty', 'Car/Truck/Van'] 
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/FVJOINEV-handler', methods=['POST'])
def FVJOINEV_handler():
    rows = connect('SELECT electric_vehicles.MUNICIPALITY, electric_vehicles.YEARS, electric_vehicles.Percent_EVs, Fuel_vehicles.Fuel_vehicle_emissions FROM Electric_Vehicles JOIN Fuel_vehicles ON electric_vehicles.MUNICIPALITY = Fuel_vehicles.MUNICIPALITY;')
    heads = ['Municipality', 'Year', 'Percent EVs', 'Fuel Vehicle Emissions'] 
    return render_template('my-result.html', rows=rows, heads=heads)

@app.route('/GHGJOINEV-handler', methods=['POST'])
def GHGJOINEV_handler():
    rows = connect('SELECT electric_vehicles.MUNICIPALITY, electric_vehicles.County, electric_vehicles.YEARS, electric_vehicles.total_personal_vehicles, electric_vehicles.no_evs, electric_vehicles.Percent_EVs, ghg.passenger_vehicle_emissions, GHG.total_mtco2e FROM Electric_Vehicles JOIN GHG ON electric_vehicles.MUNICIPALITY = GHG.MUNICIPALITY;')
    heads = ['Municipality', 'County', 'Year', 'Total Personal Vehicles', 'No of EVs', 'Percent EVs', 'Fuel Vehicle Emissions', 'Total MTCo2e'] 
    return render_template('my-result.html', rows=rows, heads=heads)

# handle venue POST and serve result web page
@app.route('/dropdown-handler', methods=['POST'])
def dropdown_handler():
    rows = connect('SELECT * FROM ' + request.form['table'] + ';')
    heads = [connect('SELECT column_name FROM information_schema.columns WHERE table_schema = ' + "'" + 'public' + "'" + 'AND table_name = ' + "'" + request.form['table'] + "'" + ';')]
    return render_template('my-result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query-handler', methods=['POST'])
def query_handler():
    rows = connect(request.form['query'])
    return render_template('my-result.html', rows=rows)

if __name__ == '__main__':
    app.run(debug = True)
