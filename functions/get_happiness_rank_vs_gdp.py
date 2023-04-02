import pandas as pd

from data.modular_read_data_variables import CSV_DATA_BACKUP
from data.modular_read_data_variables import Q4_YEAR_SELECTOR

def get_happiness_rank_vs_gdp():
    df = pd.read_csv(CSV_DATA_BACKUP)
    # Filter df by the year value
    df = df[df['year'] == Q4_YEAR_SELECTOR]
    # Sort df by Life Ladder, reset index is to avoid generate a column.
    rank_df = df.sort_values(by='Life Ladder', ascending=False).reset_index(drop=True)
    # Search the country with the max "Log GDP per capita"
    max_gdp_country = df.loc[df['Log GDP per capita'].idxmax(), 'Country name']
    # Search the raking position and sum 1 because the index begin at 0.
    position = rank_df[rank_df['Country name'] == max_gdp_country].index.tolist()[0] + 1
    return f"The country with the highest Log GDP per capita in {Q4_YEAR_SELECTOR} is {max_gdp_country}," \
           f" and it is in position {position} of the Life Ladder ranking.\n\n"
