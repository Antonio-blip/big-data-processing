import pandas as pd
from data.modular_read_data_variables import CSV_DATA_LAST_YEAR, CSV_DATA_BACKUP, Q5_YEAR_SELECTOR, LAST_YEAR

def get_world_gdp_variation():
    # Load data from world-happiness-report.csv
    df1 = pd.read_csv(CSV_DATA_BACKUP)
    # Rename columns to append properly
    df1 = df1.rename(columns={'Log GDP per capita': 'Logged GDP per capita'})

    # Load data from world-happiness-report-2021.csv
    df2 = pd.read_csv(CSV_DATA_LAST_YEAR)
    # Generate year column to group
    df2['year'] = LAST_YEAR

    # Combine both dataframes
    df = pd.concat([df1, df2], axis=0)

    # Calculate the average GDP for each year using group by and mean
    average_gdp_by_year = df.groupby('year')['Logged GDP per capita'].mean()

    # Calculate the percentage change between years
    gdp_avg_other_year = average_gdp_by_year.loc[Q5_YEAR_SELECTOR]
    gdp_avg_last_year = average_gdp_by_year.loc[LAST_YEAR]
    percentage_change = ((gdp_avg_last_year - gdp_avg_other_year) / gdp_avg_other_year) * 100

    # Return the results as a text string
    if percentage_change > 0:
        return f"The world's average GDP increased by {percentage_change:.2f}% from " + str(Q5_YEAR_SELECTOR) + " to " + str(LAST_YEAR) + ".\n\n"
    elif percentage_change < 0:
        return f"The world's average GDP decreased by {percentage_change:.2f}% from " + str(Q5_YEAR_SELECTOR) + " to " + str(LAST_YEAR) + ".\n\n"
    else:
        return "There was no change in the world's average GDP from " + str(Q5_YEAR_SELECTOR) + " to " + str(LAST_YEAR) + ".\n\n"
