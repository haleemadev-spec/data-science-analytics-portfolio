import random

import numpy as np
import pandas as pd


random.seed(42)
np.random.seed(42)

N_CUSTOMERS = 5000

countries = [
    "Senegal",
    "France",
    "United Kingdom",
    "Germany",
    "Spain",
    "Portugal",
]

records = []

for customer_id in range(1, N_CUSTOMERS + 1):

    age = random.randint(18, 65)
    country = random.choice(countries)

    tenure_months = random.randint(1, 60)

    monthly_transactions = max(
        0,
        int(np.random.normal(18, 10))
    )

    average_transaction_amount = round(
        np.random.lognormal(mean=4.7, sigma=0.45),
        2
    )

    app_sessions_monthly = max(
        1,
        int(np.random.normal(22, 12))
    )

    support_contacts = np.random.poisson(1.2)

    card_usage = max(
        0,
        int(np.random.normal(12, 7))
    )

    satisfaction_score = round(
        np.clip(np.random.normal(3.5, 0.9), 1, 5),
        1
    )

    premium_customer = int(random.random() < 0.25)

    international_transactions = max(
        0,
        int(np.random.normal(3, 3))
    )

    failed_transactions = max(
        0,
        int(np.random.poisson(1.5))
    )

    # Churn probability
    churn_score = (
        1.5
        - 0.045 * monthly_transactions
        - 0.035 * app_sessions_monthly
        - 0.35 * satisfaction_score
        - 0.015 * tenure_months
        + 0.25 * support_contacts
        + 0.20 * failed_transactions
        - 0.25 * premium_customer
    )

    churn_probability = 1 / (1 + np.exp(-churn_score))

    churn = int(random.random() < churn_probability)

    records.append(
        {
            "customer_id": customer_id,
            "age": age,
            "country": country,
            "tenure_months": tenure_months,
            "monthly_transactions": monthly_transactions,
            "average_transaction_amount": average_transaction_amount,
            "app_sessions_monthly": app_sessions_monthly,
            "support_contacts": support_contacts,
            "card_usage": card_usage,
            "satisfaction_score": satisfaction_score,
            "premium_customer": premium_customer,
            "international_transactions": international_transactions,
            "failed_transactions": failed_transactions,
            "churn": churn,
        }
    )


df = pd.DataFrame(records)

output_path = "data/customers.csv"

df.to_csv(output_path, index=False)

print(f"Generated {len(df)} customers")
print(f"Saved to {output_path}")
print(f"Churn rate: {df['churn'].mean() * 100:.2f}%")