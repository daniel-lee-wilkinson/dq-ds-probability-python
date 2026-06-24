import pandas as pd
from scipy.stats import percentileofscore
wnba = pd.read_csv("wnba.csv")

print(wnba.shape)
print(wnba)

# Frequency Distribution Tables
freq_distro_pos=wnba['Pos'].value_counts()
freq_distro_height=wnba['Height'].value_counts()
print(freq_distro_height)

# Sorting Frequency Distribution Tables
print(wnba['Height'].value_counts().sort_index())

age_ascending=wnba['Age'].value_counts().sort_index(ascending=True)
age_descending=wnba['Age'].value_counts().sort_index(ascending=False)

# Sorting Tables for Ordinal Variables
def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if (20 < row['PTS'] <= 80):
        return 'few points'
    if (80 < row['PTS'] <= 150):
        return 'many, but below average'
    if (150 < row['PTS'] <= 300):
        return 'average number of points'
    if (300 < row['PTS'] <= 450):
        return 'more than average'
    else:
        return 'much more than average'


wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis=1)

# Type your answer below

pts_ordinal_desc = wnba['PTS_ordinal_scale'].value_counts().iloc[[4, 3, 0, 2, 1, 5]]


#  Proportions and Percentages
print(wnba['Pos'].value_counts() / len(wnba)) # equivalent to setting normalise=True:
print(wnba['Pos'].value_counts(normalize = True))
print(wnba['Pos'].value_counts(normalize = True) * 100) # set as percentages

print(wnba['Age'].value_counts(normalize = True))
print(wnba['Age'].value_counts(normalize = True)*100)

# percentage over 30
percentages = wnba['Age'].value_counts(normalize = True).sort_index() * 100
percentage_over_30 = percentages.loc[30:].sum()
percentage_below_23 = percentages.loc[:23].sum()


# Percentiles and Percentile Ranks
#percentileofscore with kind="weak" gives the percentage less than and including the score value
print(percentileofscore(a=wnba['Age'], score=23, kind='weak'))
percentile_rank_half_less=percentileofscore(a=wnba['Games Played'], score=17, kind='weak')

# what percentage of scores were greater than 30?
print(100 - percentileofscore(wnba['Age'], 29, kind='weak'))
percentage_half_more=100-percentileofscore(wnba['Games Played'], score=17, kind='weak')


# Finding Percentiles with pandas

print(wnba['Age'].describe())
print(wnba['Age'].describe().iloc[3:])
print(wnba['Age'].describe(percentiles=[0.1, 0.15, 0.33, 0.5, 0.592, 0.85, 0.9]).iloc[3:])

percentiles = wnba['Age'].describe(percentiles=[0.5, 0.75, 0.95])
age_upper_quartile = percentiles['75%']
age_middle_quartile = percentiles['50%']
age_95th_percentile = percentiles['95%']


# Grouped Frequency Distribution Tables

print(wnba['Weight'].value_counts(bins=10).sort_index())
grouped_freq_table = wnba['PTS'].value_counts(bins=10, normalize=True).sort_index(ascending=False)*100


# Readability for Grouped Frequency Tables

print(wnba['PTS'].value_counts(bins=6).sort_index())

intervals = pd.interval_range(start=0, end=600, freq=100)
gr_freq_table = wnba["PTS"].value_counts(bins=intervals).sort_index()
print(gr_freq_table.sum())

intervals = pd.interval_range(start=0, end=600, freq=60)
gr_freq_table_10 = wnba["PTS"].value_counts(bins=intervals).sort_index()

# Frequency Tables and Continuous Variables

