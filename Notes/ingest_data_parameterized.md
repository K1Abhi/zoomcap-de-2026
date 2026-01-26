
```python
import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


PREFIX = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'

DTYPE = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

PARSE_DATES = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


@click.command()
@click.option("--year", default=2021, type=int, show_default=True)
@click.option("--month", default=1, type=int, show_default=True)
@click.option("--pg-user", default="root", show_default=True)
@click.option("--pg-password", default="root", show_default=True)
@click.option("--pg-host", default="localhost", show_default=True)
@click.option("--pg-port", default=5432, type=int, show_default=True)
@click.option("--pg-db", default="ny_taxi", show_default=True)
@click.option("--chunksize", default=100_000, type=int, show_default=True)
@click.option("--target-table", default="yellow_taxi_data", show_default=True)
def run(
    year,
    month,
    pg_user,
    pg_password,
    pg_host,
    pg_port,
    pg_db,
    chunksize,
    target_table,
):
    """
    Load NYC Yellow Taxi data into PostgreSQL.
    """

    url = f"{PREFIX}yellow_tripdata_{year}-{month:02d}.csv.gz"

    engine = create_engine(
        f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"
    )

    df_iter = pd.read_csv(
        url,
        dtype=DTYPE,
        parse_dates=PARSE_DATES,
        chunksize=chunksize
    )

    for i, df_chunk in enumerate(tqdm(df_iter, desc="Loading data")):
        if i == 0:
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists="replace",
                index=False
            )

        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )


if __name__ == "__main__":
    run()
```
## 1. Minimal (all defaults)
```python
python ingest.py
```
## 2. Custom database params
```python
python ingest.py \
  --pg-user root \
  --pg-password root \
  --pg-host localhost \
  --pg-port 5432 \
  --pg-db ny_taxi
```

## 3.Different month / table / chunk size\
```python
python ingest.py \
  --year 2021 \
  --month 2 \
  --target-table yellow_taxi_feb \
  --chunksize 50000
```
