import pandas as pd
import json

def transform_products(raw_products):
    #Turn the list of dicts into a table
    df = pd.DataFrame(raw_products)
    print(f"Input Shape: {df.shape}")

    #Flatten the nested rating object
    df["rating_score"] = df["rating"].apply(
        lambda x: x["rate"]
    )

    df["rating_count"] = df["rating"].apply(
        lambda x: x["count"]
    )

    # Drop the original nested column
    df = df.drop(columns=['rating'])

    # Clean the text fields
    df['title'] = df['title'].str.strip()
    df['category'] = df['category'].str.lower()

    # Round tthe prices to 2 decimal points
    df['price'] = df['price'].round(2)

    print(f"Output shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")

    return df

if __name__ == "__main__":
    with open("raw_products.json") as f:
        raw = json.load(f)

    df = transform_products(raw)
    print("\nFirst 3 Rows:")
    print(df.head(3))