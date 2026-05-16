from extract.extract import extract_products
from transform.transform import transform_products
from load.load import load_products

if __name__ == "__main__":
    print("=" * 40)
    print("  E-commerce ETL Pipeline starting")
    print("=" * 40)

    print("\n[1/3] Extracting products...")
    raw = extract_products()

    print("\n[2/3] Transforming data...")
    clean = transform_products(raw)

    print("\n[3/3] Loading to database")
    load_products(clean)

    print("\n" + "=" * 40)
    print("   Pipeline Complete")
    print("=" * 40)