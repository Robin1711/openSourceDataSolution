from pyspark.sql import SparkSession
from pyspark.sql.functions import col

LOCAL = False
spark_master = "local[*]" if LOCAL else "spark://localhost:7077"

spark = SparkSession.builder \
    .appName("PySparkTest") \
    .master(spark_master) \
    .getOrCreate()

# Create a sample DataFrame
data = [(1, "Alice", 29), (2, "Bob", 35), (3, "Charlie", 40)]
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

# Perform a transformation: Filter rows where age > 30
filtered_df = df.filter(col("age") > 30)

# Show results
filtered_df.show()

# Stop Spark Session
spark.stop()
