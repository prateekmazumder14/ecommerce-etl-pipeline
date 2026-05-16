# E-commerce ETL Pipeline

A production-style ETL pipeline built in Python that extracts product 
data from a REST API, transforms and flattens nested fields, and loads 
the cleaned data into a SQLite database with JSONL export.

Demonstrates the same ETL patterns used in a real production integration 
(Shopify → Bloomreach, 25k products, 500+ variant metafields) — 
built as the open-source equivalent using public data.

## Tech Stack

- Python 3.x
- pandas
- requests
- SQLite (via sqlite3)
- python-dotenv

## Architecture

Fake Store API (source)

↓

extract.py → raw_products.json

↓

transform.py → cleans + flattens nested fields

↓

load.py → products.db (SQLite) + products.jsonl

## How to run

```bash
git clone https://github.com/prateekmazumder14/ecommerce-etl-pipeline
cd ecommerce-etl-pipeline
pip install -r requirements.txt
python main.py
```
