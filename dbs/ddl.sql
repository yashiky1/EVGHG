CREATE TABLE GHG 
(MUNICIPALITY varchar (50) NOT NULL , 
COUNTY varchar (50) NOT NULL , 
YEARS INT NOT NULL, 
PASSENGER_VEHICLE_EMISSIONS varchar (50), 
TOTAL_MTCO2e INT, 
PRIMARY KEY (MUNICIPALITY, COUNTY, YEARS));

CREATE TABLE Community_Prof
(MUNICIPALITY varchar (50) NOT NULL , 
COUNTY varchar (50) NOT NULL , 
YEARS INT NOT NULL, 
Square_miles varchar (50),
POP INT, 
Medium_household_income varchar (50), 
Percent_pop_poverty varchar (50),
Transportation varchar (50), 
PRIMARY KEY (MUNICIPALITY, COUNTY, YEARS));

CREATE TABLE Fuel_Vehicles 
(MUNICIPALITY varchar (50) NOT NULL , 
COUNTY varchar (50) NOT NULL , 
YEARS INT NOT NULL, 
Passenger_Cars varchar (50),
Total_miles_traveled varchar (50),
Fuel_vehicle_emissions varchar (50), 
PRIMARY KEY (MUNICIPALITY, COUNTY, YEARS));

CREATE TABLE Electric_Vehicles 
(MUNICIPALITY varchar (50) NOT NULL , 
COUNTY varchar (50) NOT NULL , 
YEARS INT NOT NULL, 
Total_personal_vehicles INT NOT NULL, 
NO_EVs varchar (50), 
Percent_EVs varchar (50) NOT NULL, 
PRIMARY KEY (MUNICIPALITY, COUNTY, YEARS));



