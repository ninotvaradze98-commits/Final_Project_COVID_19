import pandas as pd

def add_vaccination_period(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a vaccination period column to the DataFrame.
    Vaccination periods are defined as "pre_vaccination" and "post_vaccination"
    Vaccination start dates are determined based on the first date of vaccination for each country.
    """
    df = df.copy()

    vaccinated = df["people_vaccinated"].fillna(0) > 0
    vaccinated_df = df[vaccinated]

    start_dates = vaccinated_df.groupby("location")["date"].min()
   
    df["vaccination_start_date"] = df["location"].map(start_dates)

    df["period"] = "pre_vaccination"
    df.loc[df["date"] >= df["vaccination_start_date"], "period"] = "post_vaccination"

    return df



def create_avg_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a table of average daily new cases before and after vaccination start date.
    The function calculates:
    - average daily new cases for pre-vaccination and post-vaccination periods
    - percentage change in average daily new cases between the two periods
    """
    avg_cases = df.groupby(["location", "period"])["new_cases"].mean().reset_index()
    avg_table = avg_cases.pivot(index="location", columns="period", values="new_cases")

    pct_change = (avg_table["post_vaccination"] - avg_table["pre_vaccination"]) / avg_table["pre_vaccination"] * 100
    avg_table["pct_change"] = pct_change
   
    return avg_table