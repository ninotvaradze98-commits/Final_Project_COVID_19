import data_loader 
import cleaning 
import pandas as pd

print("START")
df = data_loader.load_covid_data()
print("LOADED")
# print(df.columns)

df = cleaning.clean_data(df)
# print(df.head())
df = cleaning.filter_countries(df)


print(df["location"].unique())
print(df.shape)


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
