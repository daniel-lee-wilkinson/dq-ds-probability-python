import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

wnba = pd.read_csv('wnba.csv')

# Bar Plots

wnba['Pos'].value_counts().plot.bar()
plt.show()

wnba['Pos'].value_counts().plot.barh()
plt.show()


#wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]].plot.bar()
#plt.show()

#wnba["Exp_ordinal"].value_counts().iloc[[3,0,2,1,4]].plot.bar(rot=45) # rotate the x labels 45 degrees
#plt.show()

wnba['Pos'].value_counts().plot.barh(title='Number of players in WNBA by position')
plt.show()

# Pie Charts

wnba['Pos'].value_counts().plot.pie()
plt.show()

# Customizing a Pie Chart

wnba['Pos'].value_counts().plot.pie(figsize=(6,6))
plt.ylabel('')
plt.show()


wnba['Pos'].value_counts().plot.pie(figsize=(6,6), autopct='%.1f%%', title="Percentage of players in WNBA by position")
plt.show()


# Histograms

wnba['PTS'].plot.hist()
plt.show()

# The Statistics Behind Histograms
wnba['PTS'].plot.hist(grid=True, xticks=np.arange(2,585,58.2), rot=30)
plt.show()


# Histograms as Modified Bar Plots

#  Binning for Histograms
import matplotlib.pyplot as plt

wnba['PTS'].plot.hist(range=(1,600), bins=3)
plt.show()

wnba['Games Played'].plot.hist(range=(1,32), bins=8)
plt.title("The distribution of players by games played")
plt.xlabel("Games played")
plt.show()


# Skewed Distributions
wnba['AST'].plot.hist()
plt.show()
assists_distro ="right skewed"
wnba["FT%"].plot.hist()
plt.show()
ft_percent_distro = "left skewed"



# Symmetrical Distributions


wnba['Weight'].plot.hist() # normal distribution
plt.show()

wnba['BMI'].plot.hist() # slightly right skewed
plt.show()

