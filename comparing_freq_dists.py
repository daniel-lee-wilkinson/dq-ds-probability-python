import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
wnba = pd.read_csv("wnba.csv")

# Comparing Frequency Distributions
"""
# 1. segment the players in the data set by level of experience
rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']

# 2. For each segment, generate a freq dist table for the Pos variable
rookie_distro = rookies["Pos"].value_counts()
little_xp_distro = little_xp["Pos"].value_counts()
experienced_distro = experienced["Pos"].value_counts()
very_xp_distro = very_xp["Pos"].value_counts()
veteran_distro = veterans["Pos"].value_counts()

# 3. Analse the freq. dists. comparatively
"""

plt.figure().set_figwidth(8)
sns.set_theme()
"""
sns.countplot(x="Exp_ordinal", hue="Pos", data=wnba,
              order=["Rookie","Little experience", "Experienced", "Very experienced", "Veteran"],
             hue_order = ["C", "F", "F/C", "G", "G/F"])
plt.show()
"""

# Challenge: Do Older Players Play Less?


#  Comparing Histograms

wnba[wnba.Age >= 27]['MIN'].plot.hist(label='Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.hist(label='Young', legend=True)
plt.show()

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype='step', label='Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype='step', label='Young', legend=True)
plt.show()

wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype='step', label='Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype='step', label='Young', legend=True)
plt.axvline(x=497, label="Average")
plt.legend()
plt.show()


# Kernel Density Estimate Plots

wnba[wnba.Age >= 27]['MIN'].plot.kde(label='Old', legend=True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label='Young', legend=True)
plt.axvline(x=497, label="Average")
plt.legend()
plt.show()


# Drawbacks of Kernel Density Plots

wnba[wnba.Pos == 'F']['Height'].plot.kde(label='F', legend=True)
wnba[wnba.Pos == 'C']['Height'].plot.kde(label='C', legend=True)
wnba[wnba.Pos == 'G']['Height'].plot.kde(label='G', legend=True)
wnba[wnba.Pos == 'G/F']['Height'].plot.kde(label='G/F', legend=True)
wnba[wnba.Pos == 'F/C']['Height'].plot.kde(label='F/C', legend=True)
plt.show()



# Strip Plots

sns.stripplot(x='Pos', y='Height', data=wnba, hue='Pos', jitter=False)
plt.show()

sns.stripplot(x='Pos', y='Height', data=wnba, hue='Pos', jitter=True)
plt.show()

sns.stripplot(x='Pos', y='Weight', data=wnba, hue='Pos', jitter=True)
plt.show()


# Box plots
sns.set_theme()
sns.boxplot(x='Pos', y='Height', hue='Pos', data=wnba)
plt.show()


# Outliers
sns.set_theme()


iqr = 29 - 22
lower_bound = 22 - (1.5 * iqr)
upper_bound = 29 + (1.5 * iqr)
outliers_low = sum(wnba['Games Played'] < lower_bound) # True values will count as 1 in the summation
outliers_high = sum(wnba['Games Played'] > upper_bound)

sns.boxplot(wnba['Games Played'])
plt.show()
