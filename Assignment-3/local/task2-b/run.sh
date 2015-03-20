#!/bin/bash
# Run hadoop on Task 2b

rm -rf TripAmount/
chmod +x map.py reduce.py
hadoop jar /usr/local/Cellar/hadoop/2.6.0/libexec/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar \
-D mapreduce.job.reduces=1 \
-file map.py \
-mapper map.py \
-file reduce.py \
-reducer reduce.py \
-input file:///Users/brunomacedo/Desktop/Coding/Programming-Assignments/Big-Data/Assignment-3/local/task1/TripFareJoin \
-output file:///Users/brunomacedo/Desktop/Coding/Programming-Assignments/Big-Data/Assignment-3/local/task2-b/TripAmount
