import pandas as pd

DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"


def load_covid_data() -> pd.DataFrame:
    """
    Load COVID-19 dataset from local CSV file.
    """
    data = pd.read_csv(DATA_URL)
    return data

if __name__ == "__main__":
    df = load_covid_data()
    print(df.shape)