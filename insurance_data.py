import pandas as pd
import random

states = ["OH", "PA", "MI", "IN", "KY"]

data = []

for i in range(1, 501):
    age = random.randint(18, 80)
    state = random.choice(states)

    premium = random.randint(800, 3000)

    claim = random.choices(
        ["Yes", "No"],
        weights=[15, 85]
    )[0]

    if claim == "Yes":
        claim_amount = random.randint(1000, 20000)
    else:
        claim_amount = 0

    data.append([
        i,
        age,
        state,
        premium,
        claim,
        claim_amount
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Policy_ID",
        "Age",
        "State",
        "Premium",
        "Claim",
        "Claim_Amount"
    ]
)

df.to_excel(
    "insurance_claims_data.xlsx",
    index=False
)

print("Dataset created successfully!")
print(df.head())