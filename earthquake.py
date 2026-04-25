import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("earthquake.csv")
print(df)
print(df.describe())

strong = df[df["magnitude"] > 5]
print(strong)

df.plot(x="date", y="magnitude", kind="bar", title="Earthquake Magnitudes")
plt.show()

print(df.groupby("location")["magnitude"].mean())

df.groupby("location")["magnitude"].mean().plot(
    kind="bar", title="Average Magnitude by Country")
plt.show()
print(df.groupby("location")["magnitude"].max())
print(df.groupby("location")["magnitude"].max())
print(df.groupby("location")["magnitude"].count())
