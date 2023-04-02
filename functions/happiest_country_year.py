import pandas as pd
from data.modular_read_data_variables import CSV_DATA_LAST_YEAR
from data.modular_read_data_variables import LAST_YEAR

def get_happiest_country_last_year():
    data = pd.read_csv(CSV_DATA_LAST_YEAR)
    max_score = data['Ladder score'].max()
    happiest_country = data.loc[data['Ladder score'] == max_score, 'Country name'].values[0]
    return f"The happiest country in the world in {LAST_YEAR} was: {happiest_country}\n\n"