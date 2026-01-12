import pandas as pd
from analysis import add_vaccination_period

def test_add_vaccination_period_split():
    """
    Ensure pre/post vaccination periods are assigned correctly.
    """
    df = pd.DataFrame(
        {
            "date": pd.to_datetime(["2021-01-01", "2021-01-02", "2021-01-03"]),
            "location": ["Testland", "Testland", "Testland"],
            "people_vaccinated": [0, 10, 20], 
            "new_cases": [5, 6, 7],
            "new_deaths": [0, 1, 0],
        }
    )

    result = add_vaccination_period(df)
    
    assert result.loc[0, "period"] == "pre_vaccination"
    assert result.loc[1, "period"] == "post_vaccination"
    assert result.loc[2, "period"] == "post_vaccination"



