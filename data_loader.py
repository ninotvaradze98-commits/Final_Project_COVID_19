import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/govex/COVID-19/master/data_tables/vaccine_data/global_data/time_series_covid19_vaccine_global.csv"
def load_covid_data() -> pd.DataFrame:
    """
    Load COVID-19 dataset from local CSV file.
    """
    data = pd.read_csv(DATA_URL)
    return data

if __name__ == "__main__":
    df = load_covid_data()
    print(df.shape)