import os
import argparse

import pandas as pd
from sqlalchemy import create_engine #create engine to connect to database with sqlalchemy
from loguru import logger

def main(params: dict)->None:
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    green_taxi_table_name = params.green_taxi_table_name
    zone_taxi_table_name = params.zone_taxi_table_name
    green_url = params.green_url
    zone_url = params.zone_url

    green_csv_name = "green_output.csv"
    zone_csv_name = "zone_output.csv"
    
    logger.info("Getting files")
    os.system(f"wget {green_url} -O {green_csv_name}")
    os.system(f"wget {zone_url} -O {zone_csv_name}")
    logger.info("Got files")

    logger.info("Creating engine")
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    logger.info("Engine created")

    logger.info("Zone Lookup Table")
    zone_taxi = pd.read_csv(zone_csv_name) 

    logger.info("Inserting columns and rows")
    zone_taxi.head(n=0).to_sql(name=zone_taxi_table_name, con=engine, if_exists="replace") #to create columns
    zone_taxi.to_sql(name=zone_taxi_table_name, con=engine, if_exists="append") #to add rows
 
    logger.info("Green Taxi Table")
    nyc_taxi_iter = pd.read_csv(green_csv_name, compression='gzip', header=0, sep=',', iterator=True, chunksize=100000)
    nyc_taxi = next(nyc_taxi_iter)

    logger.info("Changing to timestamp")
    nyc_taxi.lpep_pickup_datetime = pd.to_datetime(nyc_taxi.lpep_pickup_datetime)
    nyc_taxi.lpep_dropoff_datetime = pd.to_datetime(nyc_taxi.lpep_dropoff_datetime)

    logger.info("Inserting columns and rows")
    nyc_taxi.head(n=0).to_sql(name=green_taxi_table_name, con=engine, if_exists="replace") #to create columns
    nyc_taxi.to_sql(name=green_taxi_table_name, con=engine, if_exists="append") #to add rows

    while True:
        try:
            nyc_taxi = next(nyc_taxi_iter)
            nyc_taxi.lpep_pickup_datetime = pd.to_datetime(nyc_taxi.lpep_pickup_datetime)
            nyc_taxi.lpep_dropoff_datetime = pd.to_datetime(nyc_taxi.lpep_dropoff_datetime)

            nyc_taxi.to_sql(name=green_taxi_table_name, con=engine, if_exists="append")
        except StopIteration:
            print('completed')
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--green_taxi_table_name', help='name of the green_taxi_table')
    parser.add_argument('--zone_taxi_table_name', help='name of the zone_taxi_table')
    parser.add_argument('--green_url', help='url of the green_taxi_csv file')
    parser.add_argument('--zone_url', help='url of the zone_taxi_csv file')

    args = parser.parse_args()
    main(args)
