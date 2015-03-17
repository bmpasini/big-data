-- ******************** Task 1 *******************
-- * Task 1.  Write a SQL query that joins the 'trips' and 'fare' table and populates a new table called 'alltrips' table. Note that the 'fares' and 'trips' tables share 4 attributes:  medallion, hack, vendor_id, pickup datetime.
-- ****************************************

CREATE VIEW alltrips AS
SELECT fares.medallion,
	   fares.hack_license,
	   fares.vendor_id,
	   rate_code,
	   store_and_fwd_flag,
	   fares.pickup_datetime,
	   dropoff_datetime,
	   passenger_count,
	   trip_time_in_secs,
	   trip_distance,
	   pickup_longitude,
	   pickup_latitude,
	   dropoff_longitude,
	   dropoff_latitude,
	   payment_type,
	   fare_amount,
	   surcharge,
	   mta_tax,
	   tip_amount,
	   tolls_amount,
	   total_amount
FROM fares INNER JOIN trips
 ON fares.medallion = trips.medallion
AND fares.hack_license = trips.hack_license
AND fares.vendor_id = trips.vendor_id
AND fares.pickup_datetime = trips.pickup_datetime;


