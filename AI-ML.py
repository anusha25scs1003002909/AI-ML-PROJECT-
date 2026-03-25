import pandas as pd
import matplotlib.pyplot as plt

data = {
    "country": ["USA", "UK", "Germany", "France", "Japan",
                "India", "Brazil", "Nigeria", "China", "Mexico"],
    "group": ["developed", "developed", "developed", "developed", "developed",
              "developing", "developing", "developing", "developing", "developing"],
    "energy_per_capita": [12000, 8000, 7500, 7000, 6500,
                          1200, 2000, 900, 3000, 2500],
    "water_per_capita": [400, 300, 320, 280, 260,
                         120, 150, 100, 180, 160],
    "material_use_per_capita": [25, 20, 18, 17, 16,
                                6, 8, 4, 10, 9]
}

df = pd.DataFrame(data)
print(df)


df["overconsumption_score"] = (
    (df["energy_per_capita"] > 6000).astype(int) +
    (df["water_per_capita"] > 250).astype(int) +
    (df["material_use_per_capita"] > 15).astype(int)
)

df["is_overconsuming"] = df["overconsumption_score"] >= 2
print(df[["country", "is_overconsuming"]])

group_avg = df.groupby("group")[["energy_per_capita", "water_per_capita", "material_use_per_capita"]].mean()
print(group_avg)

plt.bar(df["country"], df["energy_per_capita"])
plt.title("Energy Consumption per Capita")
plt.xticks(rotation=45)
plt.ylabel("kWh per person")
plt.show()


group_avg.plot(kind="bar")
plt.title("Developed vs Developing Resource Consumption")
plt.xticks(rotation=0)
plt.ylabel("Average per-capita consumption")
plt.show()

print("\nCountries consuming the most:")
print(df.sort_values("energy_per_capita", ascending=False).head())

print("\nOverconsuming countries:")
print(df[df["is_overconsuming"] == True]["country"])
