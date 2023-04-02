import pandas as pd
from data.modular_read_data_variables import CSV_DATA_LAST_YEAR
from data.modular_read_data_variables import LAST_YEAR

def get_happiest_countries_by_continent():
    # Read the CSV file
    data = pd.read_csv(CSV_DATA_LAST_YEAR)

    # Create a dictionary that maps regions to continents
    regions_to_continents = {
        'Central and Eastern Europe': 'Europe',
        'Commonwealth of Independent States': 'Europe',
        'East Asia': 'Asia',
        'Latin America and Caribbean': 'America',
        'Middle East and North Africa': 'Africa',
        'North America and ANZ': 'Oceania',
        'South Asia': 'Asia',
        'Southeast Asia': 'Asia',
        'Sub-Saharan Africa': 'Africa',
        'Western Europe': 'Europe'
    }

    # Add a 'Continent' column to the dataframe
    data['Continent'] = data['Regional indicator'].map(regions_to_continents)

    # Find the happiest country by continent
    happiest_countries_by_continent = (
        data.groupby('Continent')
        .apply(lambda x: x.loc[x['Ladder score'].idxmax()])
        [['Country name', 'Ladder score']]
    )

    # Return the results as a text string
    return f"Shown here are the countries with the highest happiness score by continent in {LAST_YEAR} \n\n" \
           f"{happiest_countries_by_continent.to_string()}\n\n"


