import data_loader 
import cleaning 
import pandas as pd
import analysis
import visualization


def main():

    df = data_loader.load_covid_data()

    df = cleaning.clean_data(df)
    df = cleaning.filter_countries(df)

    df = analysis.add_vaccination_period(df)

    df.to_csv("covid_data/cleaned_data.csv", index=False)

    avg_table = analysis.create_avg_table(df)
    avg_table.to_csv("covid_data/avg_new_cases.csv", index=False)

    visualization.create_plot_daily_new_cases(df)
    visualization.create_plot_weekly_new_cases(df)
    visualization.create_plot_avg_new_cases_comparison(avg_table)

if __name__ == "__main__":
    main()