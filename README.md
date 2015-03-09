Big Data
============================================================

Week 1 Assignment - Exploring NYC Taxi Data using SQL
---------------------------------------

The NYC Taxi & Limousine Commission (TLC) captures information about each taxi trip in the City. In this assignment, you will use mysql to 'play' with a subset of these data: trips that took place between August 1 and  August 7, 2013. You can access the data at: https://www.mediafire.com/folder/1zaqzcf722loc/taxi_data_aug_week1

Each trip contains information about pickup and dropoff location, pickup and dropoff time, and a number of other attributes including fare, tip, and distance traveled. The TLC releases the data in two files: one containing trip data and another fare data.

You will start by creating two tables, one for fares and one for trips and load the data into these tables. Here are the CREATE TABLE statements you should use:
CREATE TABLE trips (
       medallion varchar(50),
       hack_license varchar(50),
       vendor_id VARCHAR(3),
       rate_code SMALLINT,
       store_and_fwd_flag VARCHAR(3),
       pickup_datetime TIMESTAMP,
       dropoff_datetime TIMESTAMP,
       passenger_count SMALLINT,
       trip_time_in_secs INT,
       trip_distance DECIMAL(12,5),
       pickup_longitude DECIMAL(15,10),
       pickup_latitude DECIMAL(15,10),
       dropoff_longitude DECIMAL(15,10),
       dropoff_latitude DECIMAL(15,10)
);

CREATE TABLE fares (
       medallion varchar(50),
       hack_license varchar(50),
       vendor_id VARCHAR(3),
       pickup_datetime TIMESTAMP,
       payment_type VARCHAR(3),
       fare_amount DECIMAL(15,10),
       surcharge DECIMAL(15,10),
       mta_tax DECIMAL(15,10),
       tip_amount DECIMAL(15,10),
       tolls_amount DECIMAL(15,10),
       total_amount DECIMAL(15,10)
);

MySQL allows you to populate tables with data from CSV files. See the following for details: http://dev.mysql.com/doc/refman/5.1/en/load-data.html
Assuming you saved the trip data in a file called trip_data_week1.csv, you can use the following command to load the trip data into the trips table.

LOAD DATA LOCAL INFILE 'trip_data_week1.csv' 
INTO TABLE trips 
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;
 
* Task 1.  Write a SQL query that joins the 'trips' and 'fare' table and populates a new table called 'alltrips' table. Note that the 'fares' and 'trips' tables share
4 attributes:  medallion, hack, vendor_id, pickup datetime. 

* Task 2. Write the following queries in SQL to help you understand the data.

a) Find the distribution of fare amounts, i.e., for each amount A, the number of trips that cost A. The schema of the output should be: (amount, num_trips)
b) How many trips cost less than $10?
c) Find the distribution of the number of passengers.  The schema of the output should be: (number_of_passengers, num_trips)
d) Find the total revenue (for all taxis) per day. The schema of the output should be: (day, total_revenue).
e) Find the total number of trips for each taxi

* Task 3. Write SQL queries to help answer the questions below to help you identify potential problems with the data.

a) Is there more than one record for a given taxi at the same time? If there are any, what's interesting about it?
b) For each taxi, what is the percentage of trips without GPS coordinates, i.e., all 4 coordinates are recorded as 0's?
The output schema should be: (medallion, percentage_of_trips). 
c) Find the number of different taxis used by each driver. Can you identify anything unusual?

* Task 4. You will now use one additional data set that contains information about the actual vehicles used in the trips. You can obtain the data at: http://www.mediafire.com/view/6wziuzg5983q9oq/licenses.csv

Here's the schema you should use:
CREATE TABLE medallions (
       medallion varchar(50),
       name varchar(50),
       type varchar(30),
       current_status varchar(10),
       DMV_license_plate varchar(10),
       vehicle_VIN_number varchar(20),
       vehicle_type varchar(10),
       model_year DECIMAL(4),
       medallion_type varchar(30),
       agent_number INTEGER,
       agent_name varchar(30),
       agent_telephone_number varchar(15),
       agent_website varchar(50),
       agent_address varchar(50),
       last_updated_date DATE,
       last_updated_time TIME
);

a) Compare trips based on vehicle_type (WAV, HYB, CNG, LV1, DSE, NRML). 
   output schema: (vehicle_type, total_trips, total_revenue, avg_tip_percentage).
b) Compare trips based on medallion_type(Named Driver, Owner must drive). 
   output schema: (medallion_type, total_trips, total_revenue, avg_tip_percentage)
c) List the top 10 agents by total revenue.


Week 2 Assignment - Hadoop Streaming
---------------------------------------

All the tasks should be done using Hadoop Streaming (Hadoop version 2.x) and Python.
The input files (Wikipedia articles) are available at http://bigdata.poly.edu/~fchirigati/mda-class/hadoop-streaming/articles.zip
The mapper is available at http://bigdata.poly.edu/~fchirigati/mda-class/hadoop-streaming/map.py
The reducer is available at http://bigdata.poly.edu/~fchirigati/mda-class/hadoop-streaming/reduce.py

Do not forget to make the Python scripts executable by running:

  chmod +x map.py reduce.py

otherwise Hadoop Streaming may not work.

Also, when running Hadoop Streaming, make sure you only use a single reducer, i.e., make sure you use the following configuration parameter:

  -D mapreduce.job.reduces=1

The command line for Hadoop Streaming looks like the following:

  hadoop jar path-to-hadoop-streaming-jar -D mapreduce.job.reduces=1 -file map.py -mapper map.py -file reduce.py -reducer reduce.py -input path-to-input -output path-to-output

To locate where the Hadoop Streaming jar is stored in your computer, use the following command line:

  locate hadoop-streaming

Note that the command line may change depending on your MapReduce job.

Please submit a .zip file with the following structure:
  - One directory per task, named "taskX", where X is the number of the task.
  - Inside each directory, please include:
    - The Python scripts for the map and reduce phases;
    - The output directory generated by Hadoop;
    - Any other files or scripts used by your Hadoop job.
  - Please DO NOT submit the input files (Wikipedia articles).

===================================================================

Assignment - Local Hadoop Streaming

- Task 1 (CleanWordCount):
  - Modify the WordCount example to remove stop words, punctation characters, and numbers.
    A list of stop words can be found here: http://xpo6.com/wp-content/uploads/2015/01/stop-word-list.csv
    To remove the punctation, take a look at the string module in Python: https://docs.python.org/2/library/string.html
  - Output: A key-value pair per line, where key is the word, and value is the number of times the word appears in the input.
  - The output directory produced by Hadoop should be named CleanWordCount.

- Task 2 (InitialCount):
  - Modify CleanWordCount to count the number of words based on their initial (first character), i.e., count the number of words per initial.
  - The letter case should not be taken into account. For example, Apple and apple will be both counted for initial A.
  - Output: A key-value pair per line, where key is the initial (in UPPERCASE), and value is the number of words having that initial (in either uppercase or lowercase).
  - The output directory produced by Hadoop should be named InitialCount.

- Task 3 (Top-K WordCount):
  - Modify CleanWordCount to output the top 100 most frequent 7-character words, in descending order of frequency.
  - Output: A key-value pair per line, where key is the word, and value is the number of times the word appears in the input.
  - The output directory produced by Hadoop should be named TopK.

- Task 4 (InvertedIndex):
  - Modify CleanWordCount to produce an inverted index.
  - An inverted index contains, for each word, the names of the documents (i.e., files) that contain that word, and the frequency for each document. Thus, if the word "nyu" appears in documents 0010 (50 times) and 0090 (60 times), the output should be:
    nyu    0010 50, 0090 60
  - Output: A key-value pair per line, where key is the word, and value is the list of documents that contain that word (together with the frequency), separated by comma. For each key, sort the list of documents in ascending order of frequency; if more than two documents have the same frequency, use the name of the document as a tie-breaker. For instance, if "cds" appears in documents 0010 (50 times), 0000 (50 times), and 0063 (35 times), the output should be:
    cds    0063 35, 0000 50, 0010 50
  - The output directory produced by Hadoop should be named InvertedIndex.
  - Hint: During Hadoop execution, the name of the file being read by a mapper is stored in the "mapreduce_map_input_file" environment variable. In Python, you can use the os.environ to get the value of an environment variable: https://docs.python.org/2/library/os.html#os.environ