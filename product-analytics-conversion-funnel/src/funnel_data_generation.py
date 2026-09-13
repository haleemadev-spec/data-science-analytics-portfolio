import random
from datetime import datetime, timedelta

import pandas as pd

random.seed(42)

N_USERS = 5000

countries = [
    "Senegal",
    "France",
    "United Kingdom",
    "Germany",
    "Spain",
    "Portugal"
]

channels = [
    "Organic",
    "Paid Search",
    "Social Media",
    "Referral",
    "Email"
]

records = []

start_date = datetime(2025, 1, 1)

for user_id in range(1, N_USERS + 1):

    signup_date = start_date + timedelta(days=random.randint(0, 364))

    country = random.choice(countries)
    channel = random.choice(channels)

    visited = 1

    signed_up = random.random() < 0.65
    verified = signed_up and random.random() < 0.75
    funded = verified and random.random() < 0.60
    active = funded and random.random() < 0.80

    records.append(
        {
            "user_id": user_id,
            "event_date": signup_date,
            "country": country,
            "acquisition_channel": channel,
            "visited": visited,
            "signed_up": int(signed_up),
            "verified": int(verified),
            "funded": int(funded),
            "active": int(active),
        }
    )

df = pd.DataFrame(records)

df.to_csv("data/funnel_users.csv", index=False)
print(f"Generated {len(df)} users")
print("Saved to data/funnel_users.csv")