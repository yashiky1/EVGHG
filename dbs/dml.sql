SELECT * FROM electric_vehicles;

SELECT * FROM fuel_vehicles;

SELECT * FROM GHG;

SELECT * FROM Community_Prof;

SELECT Total_personal-vehicles, NO_EVs, Percent_EVs FROM electric_vehicles WHERE municipality = 'municipality name';

SELECT * FROM Community_Prof INNER JOIN electric_vehicles ON Community_Prof.YEARS = electric_vehicles.YEARS;
