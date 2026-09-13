import pandas as pd


INPUT_PATH = "data/raw/transactions_raw.csv"
OUTPUT_PATH = "data/processed/transactions_clean.csv"


def extract_data():
    """Extract raw transaction data."""
    df = pd.read_csv(INPUT_PATH)
    print(f"Extracted {len(df)} records")
    return df


def transform_data(df):
    """Clean and transform transaction data."""

    # Remove duplicate transactions
    df = df.drop_duplicates(subset=["transaction_id"])

    # Normalize text fields
    df["country"] = df["country"].fillna("Unknown")
    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    # Convert date column
    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["transaction_date"])

    # Remove invalid transaction amounts
    df = df[df["amount"] > 0]

    # Create derived analytical fields
    df["transaction_month"] = (
        df["transaction_date"]
        .dt.to_period("M")
        .astype(str)
    )

    df["is_successful"] = (
        df["status"] == "Completed"
    ).astype(int)

    print(f"Records after transformation: {len(df)}")

    return df


def validate_data(df):
    """Run data quality checks."""

    print("\nDATA QUALITY CHECKS")

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Duplicate transaction IDs: {df['transaction_id'].duplicated().sum()}")
    print(f"Missing countries: {df['country'].isna().sum()}")
    print(f"Missing transaction dates: {df['transaction_date'].isna().sum()}")
    print(f"Negative amounts: {(df['amount'] < 0).sum()}")
    print(f"Zero amounts: {(df['amount'] == 0).sum()}")

    assert df["transaction_id"].is_unique
    assert df["amount"].gt(0).all()
    assert df["transaction_date"].notna().all()

    print("Data quality validation: PASSED")


def load_data(df):
    """Load processed data to CSV."""

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"\nLoaded {len(df)} clean records")
    print(f"Saved to {OUTPUT_PATH}")


def main():
    df = extract_data()
    df = transform_data(df)
    validate_data(df)
    load_data(df)

    print("\nETL PIPELINE COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()