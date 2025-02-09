Question 1:
Question 1: What is count of records for the 2024 Yellow Taxi Data?

Answer 1:
SELECT count(*) FROM ny_taxi_external.ny_taxi;
20,332,093

Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

Answer 2:
SELECT count(distinct PULocationID) FROM `dtc-de-448913.ny_taxi_2024.external_yellow_tripdata`;
SELECT count(distinct PULocationID) FROM `dtc-de-448913.ny_taxi_2024.yellow_tripdata`;
0 MB for the External Table and 155.12 MB for the Materialized Table

Question 3:
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. 
Now write a query to retrieve the PULocationID and DOLocationID on the same table. 
Why are the estimated number of Bytes different?

Answer 3:
SELECT PULocationID FROM `dtc-de-448913.ny_taxi_2024.yellow_tripdata`;
SELECT PULocationID, DOLocationID FROM `dtc-de-448913.ny_taxi_2024.yellow_tripdata`;
BigQuery is a columnar database, and it only scans the specific columns requested in the query. 
Querying two columns (PULocationID, DOLocationID) requires reading more data 
than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

Question 4:
How many records have a fare_amount of 0?

Answer 4:
SELECT count(fare_amount) 
FROM `dtc-de-448913.ny_taxi_2024.yellow_tripdata`
WHERE fare_amount = 0;
8,333

Question 5:
What is the best strategy to make an optimized table in Big Query 
if your query will always filter based on tpep_dropoff_datetime 
and order the results by VendorID (Create a new table with this strategy)

Answer 5:
CREATE OR REPLACE TABLE ny_taxi_2024.yellow_tripdata_partitoned_clustered
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM ny_taxi_2024.external_yellow_tripdata;

Partition by tpep_dropoff_datetime and Cluster on VendorID

Question 6:
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. 
Now change the table in the from clause to the partitioned table you created for question 5 
and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.

Answer 6:
SELECT distinct VendorID FROM `dtc-de-448913.ny_taxi_2024.yellow_tripdata_partitoned_clustered`
where tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';
310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

Question 7:
Where is the data stored in the External Table you created?

Answer 7:
GCP Bucket

Question 8:
It is best practice in Big Query to always cluster your data:

Answer 8:
False

Question 9:
Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

Answer 9:
It estimates 0 bytes. Because this data (number of rows) is already available in table details from metadata.