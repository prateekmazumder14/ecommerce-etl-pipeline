# Architecture

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
