import data_loader 
import cleaning 
import pandas as pd
import matplotlib.pyplot as plt

print("START")
df = data_loader.load_covid_data()
print("LOADED")
# # print(df.columns)

df = cleaning.clean_data(df)
# # print(df.head())
df = cleaning.filter_countries(df)


# print(df["location"].unique())
# print(df.shape)


def add_vaccination_period(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    vaccinated = df["people_vaccinated"].fillna(0) > 0
    vaccinated_df = df[vaccinated]

    start_dates = vaccinated_df.groupby("location")["date"].min()
   
    df["vaccination_start_date"] = df["location"].map(start_dates)

    df["period"] = "pre_vaccination"
    df.loc[df["date"] >= df["vaccination_start_date"], "period"] = "post_vaccination"

    return df

df = add_vaccination_period(df)

print(df.groupby(["location", "period"]).size())
print(df.groupby("location")["vaccination_start_date"].first())

df.to_csv("covid_data/cleaned_data.csv", index=False)

# df = pd.read_csv(
#     "covid_data/cleaned_data.csv",
#     parse_dates=["date", "vaccination_start_date"]
# )

# average daily new cases before and after vaccination start date
avg_cases = df.groupby(["location", "period"])["new_cases"].mean().reset_index()
print(avg_cases)

avg_table = avg_cases.pivot(index="location", columns="period", values="new_cases")

pct_change = (avg_table["post_vaccination"] - avg_table["pre_vaccination"]) / avg_table["pre_vaccination"] * 100
avg_table["pct_change"] = pct_change
print(avg_table)

# Daily new cases over time by country
plt.figure()

for country in df["location"].unique():
    country_df = df[df["location"] == country]
    plt.plot(country_df["date"], country_df["new_cases"], label=country, linewidth=1)

plt.title("Daily new cases of COVID-19")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()

plt.tight_layout()
plt.savefig("covid_data/daily_new_cases.png")
plt.close()

# Weekly cases over time by country
plt.figure(figsize=(10, 6))

for country in df["location"].unique():
    country_df = df[df["location"] == country].copy()
    country_df = country_df.sort_values("date")

    country_df["weekly_cases"] = country_df["new_cases"].rolling(7).mean()

    plt.plot(country_df["date"], country_df["weekly_cases"], label=country, linewidth=1)

plt.title("Weekly new cases of COVID-19")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()

plt.tight_layout()
plt.savefig("covid_data/weekly_new_cases.png")
plt.close()

plt.figure(figsize=(8, 6))

avg_table[["pre_vaccination", "post_vaccination"]].plot(kind="bar")

plt.title("Average Daily New Cases: Pre vs Post Vaccination")
plt.xlabel("Country")
plt.ylabel("Average New Cases")

plt.tight_layout()
plt.savefig("covid_data/avg_new_cases_comparison.png")
plt.close()