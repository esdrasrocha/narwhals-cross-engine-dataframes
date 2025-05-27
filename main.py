import narwhals as nw
import pandas as pd
import polars as pl

# Choose engine: "pandas" or "polars"
engine = "polars"  # change to "pandas" if needed

# Sample data
data = {
    "name": ["Alice", "Bob", "Carla"],
    "age": [23, 35, 29]
}

# Step 1: Create native DataFrame
if engine == "pandas":
    native_df = pd.DataFrame(data)
elif engine == "polars":
    native_df = pl.DataFrame(data)
else:
    raise ValueError("Choose 'pandas' or 'polars'")

# Step 2: Convert to Narwhals DataFrame
df = nw.from_native(native_df)

# Step 3: Filter rows where age > 25
df = df.filter(df["age"] > 25)

# Step 4: Add a new column 'is_adult' (True if age >= 30)
df = df.with_columns(
    is_adult = df["age"] >= 30
)

# Step 5: Sort by age
df = df.sort("age")

# Step 6: Show result
print(f"\n🔧 Engine: {engine}")
print(df.to_native())
