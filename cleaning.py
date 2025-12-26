import pandas as pd

COUNTRIES = ["Japan", "Germany", "United States"]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df ["date"] = pd.to_datetime(df["date"])
    df = df[[
        "date",
        "location",
        "new_cases",
        "people_vaccinated",
        "people_fully_vaccinated"
    ]]
    return df

def filter_countries(df):
    return df[df["location"].isin(COUNTRIES)].copy()


if __name__ == "__main__":
    print("Data cleaning module")