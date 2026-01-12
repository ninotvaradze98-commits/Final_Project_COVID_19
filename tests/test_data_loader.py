import pandas as pd
import data_loader


def test_load_covid_data_returns_dataframe():
    """
    Test that load_covid_data returns a pandas DataFrame.
    """
    df = data_loader.load_covid_data()
    assert isinstance(df, pd.DataFrame)

def test_load_covid_data_contains_required_columns():
    """
    Test that the loaded dataset contains required columns.
    """
    df = data_loader.load_covid_data()

    required_columns = {
        "date",
        "location",
        "new_cases",
        "new_deaths",
        "people_vaccinated",
        "people_fully_vaccinated",
    }

    assert required_columns.issubset(df.columns)