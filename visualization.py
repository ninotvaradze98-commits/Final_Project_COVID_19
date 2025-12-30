import pandas as pd
import matplotlib.pyplot as plt


def create_plot_daily_new_cases(df: pd.DataFrame):
    """Create and save a plot (line chart) of daily new COVID-19 cases."""
    plt.figure()

    for country in df["location"].unique():
        country_df = df[df["location"] == country]
        plt.plot(country_df["date"], country_df["new_cases"], label=country, linewidth=1)

    start_date = country_df["vaccination_start_date"].iloc[0]
    plt.axvline(x=start_date, color="red", linestyle="--", label="Vaccination Start Date")

    plt.title("Daily new cases of COVID-19")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.tight_layout()
    plt.savefig("covid_data/daily_new_cases.png")
    plt.close()


def create_plot_weekly_new_cases(df: pd.DataFrame):
    """Create and save a plot (line chart) of weekly new COVID-19 cases."""
    plt.figure(figsize=(10, 6))

    for country in df["location"].unique():
        country_df = df[df["location"] == country].copy()
        country_df = country_df.sort_values("date")

        country_df["weekly_cases"] = country_df["new_cases"].rolling(7).mean()

        plt.plot(country_df["date"], country_df["weekly_cases"], label=country, linewidth=1)

    start_date = country_df["vaccination_start_date"].iloc[0]
    plt.axvline(x=start_date, color="red", linestyle="--", label="Vaccination Start Date")

    plt.title("Weekly new cases of COVID-19")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.legend()
    plt.tight_layout()
    plt.savefig("covid_data/weekly_new_cases.png")
    plt.close()


def create_plot_avg_new_cases_comparison(avg_table: pd.DataFrame):
    """Create and save a plot (bar chart) comparing average daily new cases pre and post vaccination."""

    plt.figure(figsize=(8, 6))

    avg_table[["pre_vaccination", "post_vaccination"]].plot(kind="bar")

    plt.title("Average Daily New Cases: Pre vs Post Vaccination")
    plt.xlabel("Country")
    plt.ylabel("Average New Cases")
    plt.tight_layout()
    plt.savefig("covid_data/avg_new_cases_comparison.png")
    plt.close()

def create_plot_avg_new_deaths_comparison(avg_deaths_table: pd.DataFrame):
    """Create and save a plot (bar chart) comparing average daily new deaths pre and post vaccination."""

    plt.figure(figsize=(8, 6))

    avg_deaths_table[["pre_vaccination", "post_vaccination"]].plot(kind="bar", width=0.8)

    plt.title("Average Daily New Deaths: Pre vs Post Vaccination")
    plt.xlabel("Country")
    plt.ylabel("Average New Deaths")
    plt.tight_layout()
    plt.savefig("covid_data/avg_new_deaths_comparison.png")
    plt.close()