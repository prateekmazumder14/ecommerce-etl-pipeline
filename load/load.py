import sqlite3
import json

def load_products(df):
    # --- Load to SQLite Database ---
    conn = sqlite3.connect("products.db")
    df.to_sql(
        "products",
        conn,
        if_exists="replace",
        index=False
    )
    conn.close()
    print(f"Loaded {len(df)} rows into products.db")
    # --- Export as JSONL ---
    with open("products.jsonl", "w") as f:
        for record in df.to_dict(orient="records"):
            f.write(json.dumps(record) + "\n")
    print(f"Exported products.jsonl")

if __name__ == "__main__":
    import pandas as pd
    from transform.transform import transform_products
    with open ("raw_products.json") as f:
        raw = json.load(f)
    df = transform_products(raw)
    load_products(df)