import requests
import pandas as pd

BASE_URL = "https://data.cms.gov/data-api/v1/dataset/92396110-2aed-4d63-a6a2-5d6207d46a29/data"

LIMIT = 1000
TARGET_ROWS = 100_000

all_rows = []
offset = 0

while len(all_rows) < TARGET_ROWS:
    params = {
        "limit": LIMIT,
        "offset": offset
    }

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Change this if your API returns rows under another key
    rows = data if isinstance(data, list) else data.get("data", [])

    if not rows:
        break

    all_rows.extend(rows)

    print(f"Downloaded {len(all_rows)} rows")

    offset += LIMIT

df = pd.DataFrame(all_rows[:TARGET_ROWS])

df.to_csv("api_100000_rows.csv", index=False)
df.to_excel("api_100000_rows.xlsx", index=False)

print("Saved api_100000_rows.csv and api_100000_rows.xlsx")
