from pyspark.sql import SparkSession
import narwhals as nw

# Step 1: Initialize Spark (Databricks already provides 'spark')
spark = SparkSession.builder \
    .appName("NarwhalsSparkExample") \
    .getOrCreate()

# Step 2: Sample data
data = [
    ("Alice", 23),
    ("Bob", 35),
    ("Carla", 29)
]

# Step 3: Create Spark DataFrame
spark_df = spark.createDataFrame(data, ["name", "age"])

# Step 4: Convert to Narwhals
df = nw.from_native(spark_df)

# Step 5: Transformations
df = df.filter(df["age"] > 25)
df = df.with_columns(is_adult = df["age"] >= 30)
df = df.sort("age")

# Step 6: Convert back to native Spark DataFrame and show result
result_df = df.to_native()
print("\n🔧 Engine: pyspark")
result_df.show()
