import sys
import pandas as pd 

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1,2], "num_passengers": [3,6]})
df['month'] = month


print(f"Running the pipeline for the month {month}")
print(df.head())

df.to_parquet(f"output_{month}.parquet")
print("Output saved in parquet format")
