# 🐋 Narwhals Cross-Engine DataFrames

This project demonstrates how to write **one single Python DataFrame logic** that runs seamlessly on:

- 🐼 **Pandas** (for local development)
- ⚡ **Polars** (for performance)
- 🔥 **PySpark** (for distributed processing)

All powered by the excellent [Narwhals](https://github.com/narwhals-dev/narwhals) library — a lightweight abstraction layer for DataFrame interoperability.

---

## 🎯 Goal

Enable data engineers and analysts to write **reusable, engine-agnostic code** using a single syntax that works across different DataFrame frameworks — from prototyping to production.

---

## 📄 Included Files

| File                 | Description                                               |
| -------------------- | --------------------------------------------------------- |
| `main.py`          | Example using Pandas with Narwhals                        |
| `requirements.txt` | Python dependencies                                       |
| `.gitignore`       | Prevents venv, cache, and system files from being tracked |

> Coming soon: examples for Polars and PySpark

---

## 🚀 How to Run (Local with Pandas)

```bash
# Clone the repository
git clone https://github.com/your-username/narwhals-cross-engine-dataframes.git
cd narwhals-cross-engine-dataframes

# Create a virtual environment
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the main script
python main.py
```
