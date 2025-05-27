import narwhals as nw
import pandas as pd

# Step 1: Create a Pandas DataFrame
data = {
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [23, 35, 29]
}
pandas_df = pd.DataFrame(data)

# Step 2: Convert to Narwhals generic DataFrame
df = nw.from_native(pandas_df)

# Step 3: Filter where age > 25
df = df.filter(df["idade"] > 25)

# ✅ Step 4: Add new column 'maior' (True if idade >= 30)
df = df.with_columns(
    maior = df["idade"] >= 30
)

# Step 5: Sort by idade
df = df.sort("idade")

# Step 6: Show result
print(df.to_native())
