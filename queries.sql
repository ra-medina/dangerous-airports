/* Finding the wildlife strikes in each year from 1990 - 1995 for both damage and no damage
incidents */ 
SELECT IncidentYear, COUNT(IncidentYear)
FROM database_discretized
WHERE AircraftDamage = 0
GROUP BY IncidentYear;

SELECT IncidentYear, COUNT(IncidentYear)
FROM database_discretized
WHERE AircraftDamage = 0
GROUP BY IncidentYear;

/* Finding wildlife strikes in each flight phase for both damage and no damage incidents */ 
SELECT FlightPhase, COUNT (FlightPhase)
FROM database_discretized
WHERE AircraftDamage = 0
GROUP BY FlightPhase;

SELECT FlightPhase, COUNT (FlightPhase)
FROM database_discretized
WHERE AircraftDamage = 1
GROUP BY FlightPhase;

/* Finding the number of aircraft damages caused by wildlife strikes by states: */ 
SELECT State, COUNT(*)
FROM database_discretized
WHERE AircraftDamage = 1
GROUP BY State;