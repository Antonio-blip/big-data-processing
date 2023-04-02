import pandas as pd
from data.modular_read_data_variables import CSV_DATA_LAST_YEAR, CSV_DATA_BACKUP, Q6_YEAR_SELECTOR, LAST_YEAR


def get_life_expectancy_change():
    # Read the World Happiness Report 2021
    df_current = pd.read_csv(CSV_DATA_LAST_YEAR)

    # Get the country with the highest Healthy life expectancy in 2021
    country_with_max_hle = df_current.loc[df_current['Healthy life expectancy'] ==
                                          max(df_current['Healthy life expectancy']), 'Country name'].values[0]

    # Read the World Happiness Report
    df_backup = pd.read_csv(CSV_DATA_BACKUP)

    # Get the life expectancy of the country with the highest Healthy life expectancy in 2019
    lfe_other_year = \
        df_backup.loc[(df_backup['Country name'] == country_with_max_hle) & (df_backup['year'] == Q6_YEAR_SELECTOR),
        'Healthy life expectancy at birth'].values[0]

    # Calculate the percentage change
    lfe_current = \
        df_current.loc[df_current['Country name'] == country_with_max_hle, 'Healthy life expectancy'].values[0]
    percent_change = ((lfe_current - lfe_other_year) / lfe_other_year) * 100

    # Determine if the life expectancy has increased or decreased
    if percent_change > 0:
        change = "increase of"
    else:
        change = "decrease of"

    result = f"There is a little life expectancy report \n" \
             f"    \u25CF The country with the highest Healthy life expectancy in 2021 is {country_with_max_hle}. \n" \
             f"    \u25CF The Healthy life expectancy for {country_with_max_hle} in {Q6_YEAR_SELECTOR} was {lfe_other_year:.2f}. " \
             f" \n " \
             f"   \u25CF The Healthy life expectancy for {country_with_max_hle} in {LAST_YEAR} is {lfe_current:.2f}. \n " \
             f"   \u25CF There has been a {change} {percent_change:.2f}% in healthy life expectancy for {country_with_max_hle} " \
             f"between {Q6_YEAR_SELECTOR} and {LAST_YEAR}. \n\n"

    return result
