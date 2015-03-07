-- ******************** Task 4 *******************

-- Let's use these indices to make the queries run faster:
CREATE INDEX trips_fares ON fares (medallion, hack_license, vendor_id, pickup_datetime);
CREATE INDEX trips_fares ON trips (medallion, hack_license, vendor_id, pickup_datetime);
ALTER TABLE medallions ADD INDEX medallion (medallion);
ALTER TABLE fares ADD INDEX medallion (medallion);

-- ****************************************
-- a) Compare trips based on vehicle_type (WAV, HYB, CNG, LV1, DSE, NRML). 
--    output schema: (vehicle_type, total_trips, total_revenue, avg_tip_percentage).
-- ****************************************

SELECT vehicle_type, COUNT(*) AS total_trips, SUM(fare_amount) AS total_revenue, CONCAT(100*SUM(tip_amount)/SUM(fare_amount), '%') AS avg_tip_percentage
FROM fares INNER JOIN trips INNER JOIN medallions
WHERE fares.medallion = trips.medallion
  AND fares.hack_license = trips.hack_license
  AND fares.vendor_id = trips.vendor_id
  AND fares.pickup_datetime = trips.pickup_datetime
  AND medallions.medallion = fares.medallion
GROUP BY vehicle_type;

-- Alternative:

-- SELECT vehicle_type, COUNT(*) AS total_trips, SUM(fare_amount) AS total_revenue, CONCAT(100*SUM(tip_amount)/SUM(fare_amount), '%') AS avg_tip_percentage
-- FROM alltrips INNER JOIN medallions
-- WHERE medallions.medallion = alltrips.medallion
-- GROUP BY vehicle_type;

-- Output:

-- +--------------+-------------+---------------------+--------------------+
-- | vehicle_type | total_trips | total_revenue       | avg_tip_percentage |
-- +--------------+-------------+---------------------+--------------------+
-- | CNG          |      110246 |  1356590.6800000000 | 0.11210875339347%  |
-- | DSE          |      155584 |  1909348.7900000000 | 0.11104553086919%  |
-- | HYB          |     1524031 | 18835301.0500000000 | 0.11131148923155%  |
-- | LV1          |      290025 |  3567208.4700000000 | 0.11143589541881%  |
-- | NRML         |       75122 |   933965.6900000000 | 0.11100409909062%  |
-- | WAV          |      138641 |  1714587.5800000000 | 0.11184258665865%  |
-- +--------------+-------------+---------------------+--------------------+
-- 6 rows in set (1 min 31.00 sec)

-- Without the indices it took (28 min 21.68 sec).


-- ****************************************
-- b) Compare trips based on medallion_type(Named Driver, Owner must drive). 
--    output schema: (medallion_type, total_trips, total_revenue, avg_tip_percentage)
-- ****************************************

SELECT medallion_type, COUNT(*) AS total_trips, SUM(fare_amount) AS total_revenue, CONCAT(SUM(tip_amount)/SUM(fare_amount), '%') AS avg_tip_percentage
FROM fares INNER JOIN trips INNER JOIN medallions
WHERE fares.medallion = trips.medallion
  AND fares.hack_license = trips.hack_license
  AND fares.vendor_id = trips.vendor_id
  AND fares.pickup_datetime = trips.pickup_datetime
  AND medallions.medallion = fares.medallion
GROUP BY medallion_type;

-- Alternative:

-- SELECT medallion_type, COUNT(*) AS total_trips, SUM(fare_amount) AS total_revenue, CONCAT(100*SUM(tip_amount)/SUM(fare_amount), '%') AS avg_tip_percentage
-- FROM alltrips INNER JOIN medallions
-- WHERE medallions.medallion = alltrips.medallion
-- GROUP BY medallion_type;

-- Output:

-- +------------------+-------------+---------------------+--------------------+
-- | medallion_type   | total_trips | total_revenue       | avg_tip_percentage |
-- +------------------+-------------+---------------------+--------------------+
-- | NAMED DRIVER     |     1611277 | 19921508.0400000000 | 0.11132526842581%  |
-- | OWNER MUST DRIVE |      682372 |  8395494.2200000000 | 0.11147426172607%  |
-- +------------------+-------------+---------------------+--------------------+
-- 2 rows in set (1 min 25.94 sec)

-- Without the indices it took (22 min 32.15 sec).


-- ****************************************
-- c) List the top 10 agents by total revenue.
-- ****************************************

SELECT agent_name, SUM(fare_amount) AS revenue
FROM fares INNER JOIN medallions
WHERE fares.medallion = medallions.medallion
GROUP BY agent_number
ORDER BY revenue DESC LIMIT 10;

-- +-------------------------------+--------------------+
-- | agent_name                    | revenue            |
-- +-------------------------------+--------------------+
-- | TIRU CABS                     | 9133120.0500000000 |
-- | ALL TAXI MANAGEMENT INC       | 1672496.6000000000 |
-- | TAXIFLEET MANAGEMENT LLC      | 1237792.8700000000 |
-- | TEAM SYSTEMS CORP             |  797958.4100000000 |
-- | WOODSIDE MANAGEMENT INC.      |  770086.9000000000 |
-- | OLA CABS                      |  764637.1600000000 |
-- | WHITE AND BLUE GROUP CORP.    |  666874.3800000000 |
-- | MC GUINNESS MANAGEMENT CORP   |  652309.6000000000 |
-- | EXECUTIVE OWNERS HOLDING CORP |  617902.6900000000 |
-- | QUEENS MEDALLION LEASING INC. |  604641.4500000000 |
-- +-------------------------------+--------------------+
-- 10 rows in set (1 min 8.87 sec)

