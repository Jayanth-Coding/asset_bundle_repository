from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.table(comment="Number of trips and average fare per day")
@dp.expect("fare_is_positive", "avg_fare>0")
@dp.expect_or_drop("busy_day", "trip_count>350")
def daily_trip_stats():
    return (
        spark.read.table("sample_trips_my_bundle_init_project")
        .groupBy(F.to_date("tpep_pickup_datetime").alias("trip_date"))
        .agg(F.count("*").alias("trip_count"), F.round(F.avg("fare_amount"), 2).alias("avg_fare"))
    )
