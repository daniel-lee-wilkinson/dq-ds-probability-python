# Variables in Statistics

import pandas as pd
wnba = pd.read_csv('wnba.csv')


# quantitative vs qualitative variables
variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative',
             'Height': 'quantitative', 'BMI': 'quantitative',
             'Birth_Place': 'qualitative', 'Birthdate': 'quantitative', 'Age': 'quantitative',
             'College': 'qualitative', 'Experience': 'quantitative', 'Games Played': 'quantitative',
             'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
             '3PA': 'quantitative', 'FTM': 'quantitative',
             'FTA': 'quantitative', 'FT%': 'quantitative', 'OREB': 'quantitative', 'DREB': 'quantitative',
             'REB': 'quantitative', 'AST': 'quantitative', 'PTS': 'quantitative'}

# Nominal scale

nominal_scale = sorted(['Name', 'Team', 'Pos', 'Birth_Place', 'College'])

# Ordinal scale (has direction e.g. ranks)

# The Interval and Ratio Scales (e.g. price, weight, height)

# The difference between ratio and interval scales

# e.g. weight = 89kg, ratio = weight_deviation
# i.e. 10.234 meaning baseline +/- 10.234kg
interval = ['Birthdate', 'Weight_deviation']
ratio = sorted(['Height', 'Weight', 'BMI', 'Age', 'Experience', 'Games Played', 'MIN', 'FGM', 'FGA', 'FG%', '15:00',
                '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO',
                'PTS', 'DD2', 'TD3'])


# Common examples of interval scales
# temperature (deg C), temp (K), temp (deg F)


# Discrete and Continuous Variables
ratio_interval_only = {'Height':'', 'Weight': '', 'BMI': '', 'Age': '', 'Games Played': '', 'MIN': '', 'FGM': '',
                       'FGA': '', 'FG%': '', '3PA': '', '3P%': '', 'FTM': '', 'FTA': '', 'FT%': '',
                       'OREB': '', 'DREB': '', 'REB': '', 'AST': '', 'STL': '', 'BLK': '', 'TO': '',
                       'PTS': '', 'DD2': '', 'TD3': '', 'Weight_deviation': ''}


ratio_interval_only = {'Height': 'continuous', 'Weight': 'continuous', 'BMI': 'continuous', 'Age': 'continuous',
                       'Games Played': 'discrete', 'MIN': 'continuous', 'FGM': 'discrete',
                       'FGA': 'discrete', 'FG%': 'continuous', '3PA': 'discrete', '3P%': 'continuous',
                       'FTM': 'discrete', 'FTA': 'discrete', 'FT%': 'continuous', 'OREB': 'discrete',
                       'DREB': 'discrete', 'REB': 'discrete', 'AST': 'discrete', 'STL': 'discrete',
                       'BLK': 'discrete', 'TO': 'discrete', 'PTS': 'discrete', 'DD2': 'discrete',
                       'TD3': 'discrete', 'Weight_deviation': 'continuous'}


# Real limits
bmi = {21.201: [],
 21.329: [],
 23.875: [],
 24.543: [],
 25.469: []}


bmi = {21.201: [21.2005, 21.2015],
 21.329: [21.3285, 21.3295],
 23.875: [23.8745, 23.8755],
 24.543: [24.5425, 24.5435],
 25.469: [25.4685, 25.4695]}







