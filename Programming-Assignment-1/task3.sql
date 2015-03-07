-- ******************** Task 3 *******************
-- * Task 3. Write SQL queries to help answer the questions below to help you identify potential problems with the data.
-- ****************************************

-- ****************************************
-- a) Is there more than one record for a given taxi at the same time? If there are any, what's interesting about it?
-- ****************************************

-- The query below show all taxis that have more than one record with the same pickup time
SELECT medallion, hack_license, vendor_id, pickup_datetime, COUNT(*)
FROM trips
GROUP BY medallion, pickup_datetime
HAVING COUNT(*) > 1;

-- The result was positive and from the query above I picked one taxi as an example
SELECT medallion, pickup_datetime
FROM trips
WHERE medallion = "002B4CFC5B8920A87065FC131F9732D1"
GROUP BY medallion, pickup_datetime
HAVING COUNT(*) > 1;

-- Then, I queried for that taxi and the result is that is has two equal records with the same pickup time, but different dropoff time
SELECT medallion, hack_license, vendor_id, pickup_datetime, dropoff_datetime
FROM trips
WHERE medallion = "002B4CFC5B8920A87065FC131F9732D1"
  AND pickup_datetime = "2013-08-06 15:41:00";

-- So, I queried for taxis that have more than one record with the same pickup time and dropoff time
SELECT medallion, hack_license, vendor_id, pickup_datetime, dropoff_datetime, COUNT(*)
FROM trips
GROUP BY medallion, pickup_datetime, dropoff_datetime
HAVING COUNT(*) > 1;

-- It turns out that the result had 25 different rows. Most of them had the pickup time equal to the dropoff time, so it might be that the taxi driver started these runs by mistake. For the other cases, I went ahead and picked one sample to check if it was really a duplicate entry.
SELECT *
FROM trips
WHERE medallion = "7B501672204EB6B8777CE5C16296AC66"
  AND pickup_datetime = "2013-08-03 23:11:10"
  AND dropoff_datetime = "2013-08-03 23:16:16";

-- And the sample I got was in fact a duplicate entry.
-- Therefore, we can conclude that there are indeed inconsistencies in the data and one interesting thing about it is that it seems like that people can be charged multiple times for a ride due to umpredictable technical failures.


-- ****************************************
-- b) For each taxi, what is the percentage of trips without GPS coordinates, i.e., all 4 coordinates are recorded as 0's?
-- The output schema should be: (medallion, percentage_of_trips). 
-- ****************************************

-- Let's use this index to make the query run faster:
CREATE INDEX trips_geo ON trips (pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude);

SELECT t1.medallion, CONCAT(100 * no_gps_trips_count / all_trips_count, '%') AS percentage_of_trips
FROM ((SELECT medallion, COUNT(*) AS no_gps_trips_count
	   FROM trips
	   WHERE pickup_longitude = 0
     	 AND pickup_latitude = 0
		 AND dropoff_longitude = 0
		 AND dropoff_latitude = 0
	   GROUP BY medallion) AS t1
INNER JOIN (SELECT medallion, COUNT(*) AS all_trips_count
			FROM trips
			GROUP BY medallion) AS t2)
WHERE t1.medallion = t2.medallion;


-- ****************************************
-- c) Find the number of different taxis used by each driver. Can you identify anything unusual?
-- ****************************************

SELECT hack_license, COUNT(DISTINCT medallion)
FROM trips
GROUP BY hack_license;

-- Yes, some drivers drove more than 1 taxi during that week.


