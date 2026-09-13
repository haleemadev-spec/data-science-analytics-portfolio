import random

import numpy as np
import pandas as pd


random.seed(42)
np.random.seed(42)

N_TRANSACTIONS = 15000

countries = [
    "Senegal",
    "France",
    "United Kingdom",
    "Germany",
    "Spain",
    "Portugal",
]

transaction_types = [
    "Card Payment",
    "Transfer",
    "Cash Withdrawal",
    "Online Payment",
]

devices = [
    "Mobile",
    "Web",
    "Tablet",
]

records = []

for transaction_id in range(1, N_TRANSACTIONS + 1):

    customer_id = random.randint(1, 4000)

    transaction_amount = round(
        np.random.lognormal(mean=4.8, sigma=0.8),
        2
    )

    country = random.choice(countries)
    transaction_type = random.choice(transaction_types)
    device = random.choice(devices)

    transaction_hour = random.randint(0, 23)

    customer_transaction_count = max(
        1,
        int(np.random.normal(20, 10))
    )

    customer_average_amount = round(
        np.random.lognormal(mean=4.7, sigma=0.6),
        2
    )

    international_transaction = int(
        random.random() < 0.15
    )

    failed_transactions = np.random.poisson(1.5)

    fraud_score = (
        -5.0
        + 0.003 * transaction_amount
        + 0.8 * international_transaction
        + 0.7 * int(transaction_hour < 5)
        + 0.15 * failed_transactions
        + 0.0008 * max(
            0,
            transaction_amount - customer_average_amount
        )
    )

    fraud_probability = 1 / (
        1 + np.exp(-fraud_score)
    )

    fraud = int(
        random.random() < fraud_probability
    )

    records.append(
        {
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "transaction_amount": transaction_amount,
            "country": country,
            "transaction_type": transaction_type,
            "device": device,
            "transaction_hour": transaction_hour,
            "customer_transaction_count": customer_transaction_count,
            "customer_average_amount": customer_average_amount,
            "international_transaction": international_transaction,
            "failed_transactions": failed_transactions,
            "fraud": fraud,
        }
    )


df = pd.DataFrame(records)

output_path = "data/transactions.csv"

df.to_csv(output_path, index=False)

print(f"Generated {len(df)} transactions")
print(f"Saved to {output_path}")
print(f"Fraud rate: {df['fraud'].mean() * 100:.2f}%")
