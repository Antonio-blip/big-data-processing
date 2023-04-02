import pandas as pd
from data.modular_read_data_variables import CSV_DATA_LAST_YEAR
from data.modular_read_data_variables import CSV_DATA_BACKUP
from data.modular_read_data_variables import LAST_YEAR


def get_max_score_countries_by_year():
    # Load data from world-happiness-report.csv
    df1 = pd.read_csv(CSV_DATA_BACKUP)
    # Rename columns to append properly
    df1 = df1.rename(columns={'Life Ladder': 'Ladder score'})

    # Load data from world-happiness-report-2021.csv
    df2 = pd.read_csv(CSV_DATA_LAST_YEAR)
    # Generate year column to group
    df2['year'] = LAST_YEAR

    # Combine both dataframes
    df = pd.concat([df1, df2], axis=0)

    # Group by year and country and get max score
    grouped = df.groupby(['year', 'Country name'])['Ladder score'].max()

    # Find the country with the highest Ladder score for each year
    max_scores = df.groupby(['year'])[['Country name', 'Ladder score']].apply(
        lambda x: x.loc[x['Ladder score'].idxmax()])

    # Count how many times each country appears in the previous results and sort it
    count = max_scores.groupby('Country name').size().sort_values(ascending=False)
    # Add name to the generated count
    top_5 = count.head(5).to_frame().reset_index().set_axis(['Country', 'Total times'], axis=1, copy=False)

    # Variable to get the max number of top values
    max_count = count.max()

    # It secures we got the data properly
    if count.empty:
        return "No country appeared more than once in the list of maximum scores."

    # Which country or countries have more top scores over the years
    most_common_countries = count[count == count.max()].index.tolist()

    # Create the output string
    output = "These are the data of the countries that have obtained the best score and how many times they have " \
             "obtained them along the years\n\n"
    output += top_5.head().to_string(index=False) + "\n"
    output += "\n   \u25CF That is to say, the country/countries that held first place for the most years is/are: "
    # Join the most common_countries list into a string separated by ","
    output += ", ".join(most_common_countries) + ".\n"
    output += "   \u25CF The maximum number of times the highest score has been achieved is: " + str(max_count) + "\n\n"

    return output
