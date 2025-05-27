import narwhals as nw
import pandas as pd
import polars as pl
import argparse

# 📌 Parse engine from command-line argument
parser = argparse.ArgumentParser()
parser.add_argument("--engine", choices=["pandas", "polars"], default="pandas", help="Choose which engine to run")
args = parser.parse_args()

engine = args.engine

# Sample data
data = {
    "name": ["Alice", "Bob", "Carla"],
    "age": [23, 35, 29]
}

# Native DataFrame
if engine == "pandas":
    native_df = pd.DataFrame(data)
elif engine == "polars":
    native_df = pl.DataFrame(data)

# Transformations using Narwhals
df = nw.from_native(native_df)
df = df.filter(df["age"] > 25)
df = df.with_columns(is_adult = df["age"] >= 30)
df = df.sort("age")

# Output
print(f"\n🔧 Engine: {engine}")
print(df.to_native())
