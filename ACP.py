
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the built-in planets dataset
planets = sns.load_dataset("planets")

# 2. Inspect the dataset
print("First five rows:")
print(planets.head())

print("\nDataset information:")
planets.info()

print("\nStatistical summary:")
print(planets.describe())

print("\nMissing values:")
print(planets.isnull().sum())

# Remove rows with missing values for the relevant charts
data = planets.dropna(subset=["year", "method", "orbital_period"])

# 3. Planet discoveries by year
plt.figure(figsize=(10, 5))
sns.histplot(data=data, x="year", binwidth=5, color="royalblue")
plt.title("Planet Discoveries Over Time")
plt.xlabel("Discovery Year")
plt.ylabel("Number of Planet Records")
plt.tight_layout()
plt.show()

# 4. Discoveries by detection method
plt.figure(figsize=(10, 6))
sns.countplot(
    data=data,
    y="method",
    order=data["method"].value_counts().index,
    color="teal"
)
plt.title("Planet Discoveries by Method")
plt.xlabel("Number of Planet Records")
plt.ylabel("Discovery Method")
plt.tight_layout()
plt.show()

# 5. Distribution of orbital periods
plt.figure(figsize=(10, 5))
sns.histplot(
    data=data,
    x="orbital_period",
    bins=40,
    color="orange"
)
plt.title("Distribution of Planet Orbital Periods")
plt.xlabel("Orbital Period (days)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 6. Orbital period by discovery method
plt.figure(figsize=(12, 6))
sns.boxplot(
    data=data,
    x="method",
    y="orbital_period",
    color="lightgreen"
)
plt.title("Orbital Period by Discovery Method")
plt.xlabel("Discovery Method")
plt.ylabel("Orbital Period (days)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
