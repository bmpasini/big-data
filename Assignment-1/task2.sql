-- ******************** Task 2 *******************
-- * Task 2. Write the following queries in SQL to help you understand the data.
-- ****************************************

-- ****************************************
-- a) Find the distribution of fare amounts, i.e., for each amount A, the number of trips that cost A. The schema of the output should be: (amount, num_trips)
-- ****************************************

SELECT fare_amount AS amount, COUNT(*) AS num_trips
FROM fares
GROUP BY fare_amount;

-- For a more significant result, which would exclude some anomalies:
-- SELECT fare_amount AS amount, COUNT(*) AS num_trips FROM fares GROUP BY fare_amount HAVING COUNT(*) > 5 AND amount > 0;


-- ****************************************
-- b) How many trips cost less than $10?
-- ****************************************

SELECT COUNT(*) AS num_trips
FROM fares
WHERE total_amount < 10;


-- ****************************************
-- c) Find the distribution of the number of passengers. The schema of the output should be: (number_of_passengers, num_trips)
-- ****************************************

SELECT passenger_count AS number_of_passengers, COUNT(*) AS num_trips
FROM trips
GROUP BY passenger_count;


-- ****************************************
-- d) Find the total revenue (for all taxis) per day. The schema of the output should be: (day, total_revenue).
-- ****************************************

SELECT DATE(pickup_datetime) AS day, SUM(total_amount) AS total_revenue
FROM fares
GROUP BY DATE(pickup_datetime);


-- ****************************************
-- e) Find the total number of trips for each taxi
-- ****************************************

SELECT medallion, COUNT(*) AS number_of_trips
FROM trips
GROUP BY medallion;

-- Or this, depending on what uniquely identifies one taxi:
-- SELECT medallion, hack_license, vendor_id, COUNT(*) AS number_of_trips FROM trips GROUP BY medallion, hack_license, vendor_id;

