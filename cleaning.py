import pandas as pd

COUNTRIES = ["Japan", "Germany", "United States"]

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare COVID-19 data for analysis.
    Converts date column to datetime and filters relevant columns.
    """
    df = df.copy()
    df ["date"] = pd.to_datetime(df["date"])
    df = df[[
        "date",
        "location",
        "new_cases",
        "new_deaths",
        "people_vaccinated",
        "people_fully_vaccinated"
    ]]
    return df

def filter_countries(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the DataFrame to include only the specified countries.
    """
    return df[df["location"].isin(COUNTRIES)].copy()


