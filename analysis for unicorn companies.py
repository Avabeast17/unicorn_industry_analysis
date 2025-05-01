# Unicorn Industry Analysis (2019–2021)
# Python + SQL + pandas project for analyzing top-performing unicorn industries

import pandas as pd

# Simulated merged data from multiple tables (for teaching purposes)
data = {
    "company_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "industry": ["Fintech", "AI", "Fintech", "E-commerce", "AI", "E-commerce", "Fintech", "AI", "Healthtech", "E-commerce", "Healthtech", "AI"],
    "date_joined": ["2020-05-10", "2019-07-15", "2021-01-20", "2020-03-05", "2021-09-10", "2021-06-18", "2019-10-30", "2020-12-25", "2021-04-01", "2019-02-17", "2020-11-11", "2021-08-01"],
    "valuation": [1200000000, 950000000, 2300000000, 1800000000, 1500000000, 2000000000, 1000000000, 1100000000, 1250000000, 1750000000, 1350000000, 1050000000]
}

# Create DataFrame Here
df_all = pd.DataFrame(data)

# Step 1: Extract year from date_joined
df_all["year"] = pd.to_datetime(df_all["date_joined"]).dt.year

# Step 2: Filter years of interest
df_filtered = df_all[df_all["year"].isin([2019, 2020, 2021])]

# Step 3: Identify top 3 industries by number of unicorns
top_industries = (
    df_filtered.groupby("industry")
    .size()
    .sort_values(ascending=False)
    .head(3)
    .index.tolist()
)

# Step 4: Filter only those industries
df_top = df_filtered[df_filtered["industry"].isin(top_industries)]

# Step 5: Aggregate by industry and year
summary = (
    df_top
    .groupby(["industry", "year"])
    .agg(num_unicorns=("company_id", "count"),
         average_valuation_billions=("valuation", lambda x: round(x.mean() / 1e9, 2)))
    .reset_index()
    .sort_values(by=["year", "num_unicorns"], ascending=[False, False])
)

# Final DataFrame to export
df = summary
print(df)

