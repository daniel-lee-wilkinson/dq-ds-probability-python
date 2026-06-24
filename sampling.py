import pandas as pd
import matplotlib.pyplot as plt
wnba = pd.read_csv('wnba.csv')
print(wnba.head(5))
print(wnba.tail(5))
print(wnba.shape)

parameter = wnba["Games Played"].max()
print(f"The maximum number of games played is: {parameter}")

sample = wnba["Games Played"].sample(30, random_state=1)

statistic = sample.max()

sampling_error = parameter - statistic

sample = wnba["PTS"].sample(10, random_state=1)

sample_means = []
for i in range(100):
    sample = wnba["PTS"].sample(10, random_state=i)
    sample_means.append(sample.mean())

import matplotlib.pyplot as plt

plt.scatter(x=range(1, 101), y=sample_means)
plt.axhline(wnba["PTS"].mean())
plt.show()

wnba["points_per_game"]=wnba["PTS"]/wnba["Games Played"]
# 2) Stratify by position (Pos)
g_stratum = wnba[wnba["Pos"] == "G"]
f_stratum = wnba[wnba["Pos"] == "F"]
c_stratum = wnba[wnba["Pos"] == "C"]
gf_stratum = wnba[wnba["Pos"] == "G/F"]
fc_stratum = wnba[wnba["Pos"] == "F/C"]

# Put strata in a dict so we can loop cleanly
strata = {
    "G": g_stratum,
    "F": f_stratum,
    "C": c_stratum,
    "G/F": gf_stratum,
    "F/C": fc_stratum,
}

# 3) Loop: sample 10 from each stratum, compute mean PPG, store in dict
mean_ppg_by_pos = {}

for pos, df_pos in strata.items():
    # If a stratum has < 10 rows, sample all rows (otherwise .sample(10) errors)
    n = min(10, len(df_pos))
    sample = df_pos.sample(n=n, random_state=0)
    mean_ppg_by_pos[pos] = sample["points_per_game"].mean()

# 4) Find the position with the highest mean points per game
position_most_points = max(mean_ppg_by_pos, key=mean_ppg_by_pos.get)

position_most_points, mean_ppg_by_pos

under_12 = wnba[wnba["Games Played"] <= 12]
btw_13_22 = wnba[(wnba["Games Played"] > 12) & (wnba["Games Played"] <= 22)]
over_22 = wnba[wnba["Games Played"] > 22]

proportional_sampling_means = []

for i in range(100):
    sample_under_12 = under_12["PTS"].sample(1, random_state=i)
    sample_btw_13_22 = btw_13_22["PTS"].sample(2, random_state=i)
    sample_over_23 = over_22["PTS"].sample(7, random_state=i)

    final_sample = pd.concat([sample_under_12, sample_btw_13_22, sample_over_23])
    proportional_sampling_means.append(final_sample.mean())

from matplotlib import pyplot as plt

plt.scatter(x=range(1, 101), y=proportional_sampling_means)
plt.axhline(wnba["PTS"].mean())
plt.show()

print(wnba['MIN'].value_counts(bins=3, normalize=True))

clusters = pd.Series(wnba['Team'].unique()).sample(4, random_state=0)

sample = pd.DataFrame()

for cluster in clusters:
    data_collected = wnba[wnba['Team'] == cluster]
    sample = pd.concat([sample, data_collected])

sampling_error_height = wnba['Height'].mean() - sample['Height'].mean()
sampling_error_age = wnba['Age'].mean() - sample['Age'].mean()
sampling_error_BMI = wnba['BMI'].mean() - sample['BMI'].mean()
sampling_error_points = wnba['PTS'].mean() - sample['PTS'].mean()

