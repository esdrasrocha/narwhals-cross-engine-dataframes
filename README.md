# 🐋 Narwhals Cross-Engine DataFrames

This project demonstrates how to write **a single Python DataFrame logic** that runs seamlessly on:

- 🐼 **Pandas** (for local development)
- ⚡ **Polars** (for high performance)
- 🔥 **PySpark** (coming soon)

All powered by the excellent [Narwhals](https://github.com/narwhals-dev/narwhals) library — a lightweight abstraction for DataFrame interoperability.

---

## 🎯 Goal

Allow engineers and analysts to write **portable, reusable data transformation code** that runs on multiple engines without rewriting logic.

---

## 📄 Files

| File                 | Description                             |
| -------------------- | --------------------------------------- |
| `main.py`          | Unified example using Pandas and Polars |
| `requirements.txt` | Python dependencies                     |
| `.gitignore`       | Ignore `venv/`, caches, system files  |

> PySpark version coming soon in `3-spark.py`

---

## 🧠 What the Code Does

- Loads sample data with names and ages
- Filters rows where `age > 25`
- Adds a new column `is_adult` (True if age ≥ 30)
- Sorts by age
- Prints the result

Output example:
