from pathlib import Path
import csv
import random
from datetime import datetime, timedelta

# Reproducible dataset
random.seed(42)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = DATA_DIR / "transactions.csv"

# Dataset configuration
NUMBER_OF_CUSTOMERS = 1000
NUMBER_OF_TRANSACTIONS = 15000

COUNTRIES = ["Senegal", "France", "UK", "Germany", "Spain", "Portugal"]
CUSTOMER_SEGMENTS = ["Standard", "Premium", "Business"]
TRANSACTION_TYPES = ["Card Payment", "Transfer", "Cash Withdrawal", "Online Payment"]
MERCHANT_CATEGORIES = [
    "Groceries",
    "Transport",
    "Restaurants",
    "Utilities",
    "Shopping",
    "Entertainment",
    "Travel",
    "Healthcare",
]

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)


def random_date():
    days_range = (END_DATE - START_DATE).days
    random_days = random.randint(0, days_range)
    random_seconds = random.randint(0, 86399)

    return START_DATE + timedelta(
        days=random_days,
        seconds=random_seconds
    )


def generate_customers():
    customers = []

    for customer_id in range(1, NUMBER_OF_CUSTOMERS + 1):
        country = random.choices(
            COUNTRIES,
            weights=[35, 20, 15, 10, 10, 10]
        )[0]

        segment = random.choices(
            CUSTOMER_SEGMENTS,
            weights=[70, 25, 5]
        )[0]

        age = random.randint(18, 70)

        customers.append({
            "customer_id": customer_id,
            "country": country,
            "segment": segment,
            "age": age,
        })

    return customers


def generate_transactions(customers):
    transactions = []

    for transaction_id in range(1, NUMBER_OF_TRANSACTIONS + 1):
        customer = random.choice(customers)

        transaction_type = random.choices(
            TRANSACTION_TYPES,
            weights=[50, 20, 10, 20]
        )[0]

        merchant_category = random.choice(MERCHANT_CATEGORIES)

        # Transaction amount in EUR
        if customer["segment"] == "Business":
            amount = random.uniform(20, 1200)
        elif customer["segment"] == "Premium":
            amount = random.uniform(10, 600)
        else:
            amount = random.uniform(5, 300)

        # Small probability of unusually large transactions
        if random.random() < 0.02:
            amount *= random.uniform(3, 8)

        transaction_date = random_date()

        transactions.append({
            "transaction_id": transaction_id,
            "customer_id": customer["customer_id"],
            "transaction_date": transaction_date.strftime("%Y-%m-%d %H:%M:%S"),
            "transaction_type": transaction_type,
            "merchant_category": merchant_category,
            "amount_eur": round(amount, 2),
            "country": customer["country"],
            "customer_segment": customer["segment"],
        })

    return transactions


def save_transactions(transactions):
    fieldnames = [
        "transaction_id",
        "customer_id",
        "transaction_date",
        "transaction_type",
        "merchant_category",
        "amount_eur",
        "country",
        "customer_segment",
    ]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(transactions)


def main():
    print("Generating customers...")
    customers = generate_customers()

    print("Generating transactions...")
    transactions = generate_transactions(customers)

    print("Saving dataset...")
    save_transactions(transactions)

    print()
    print("Dataset generated successfully.")
    print(f"Customers: {len(customers)}")
    print(f"Transactions: {len(transactions)}")
    print(f"File: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()