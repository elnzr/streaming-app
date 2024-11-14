from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import *


def main():
    spark = (
        SparkSession.builder
            .appName("Pyspark Streaming example")
            .getOrCreate()
    )

    host = "127.0.0.1"
    port = "9999"

    df = (
        spark.readStream
            .format("socket")
            .option("host", host)
            .option("port", port)
            .load()
    )
    msg_schema = StructType([
        StructField("user_id", StringType()),
        StructField("new_followers", IntegerType())
    ])
    messages = (
        df.select(F.explode(F.split(df.value, "\n")).alias("msg"))
           .select(F.from_json(F.col("msg"), msg_schema).alias("user"))
           .select("user.*")
    )
    agg_df = (
        messages.groupBy("user_id")
            .sum("new_followers")
    )
    query = agg_df \
        .writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()

    query.awaitTermination()


if __name__ == '__main__':
    main()