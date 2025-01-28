import pandas as pd

green_csv_name = "green_output.csv"
nyc_taxi_iter = pd.read_csv(green_csv_name, compression='gzip', header=0, sep=',', iterator=True, chunksize=100000)
nyc_taxi = next(nyc_taxi_iter)

print(nyc_taxi.columns)