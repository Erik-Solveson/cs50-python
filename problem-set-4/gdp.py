import requests
import matplotlib.pyplot as plt
import pandas as pd

# World Bank API endpoint for GDP data (replace with correct API or dataset)
WORLD_BANK_API = "http://api.worldbank.org/v2/country/{country}/indicator/NY.GDP.MKTP.CD?format=json&date=1945:2024"

# Function to fetch GDP data
def fetch_gdp_data(country_code):
    response = requests.get(WORLD_BANK_API.format(country=country_code))
    data = response.json()

    if len(data) < 2 or "value" not in data[1][0]:
        raise ValueError("Invalid data received from API")

    # Extract years and GDP values
    gdp_data = {entry["date"]: entry["value"] for entry in data[1] if entry["value"] is not None}
    return pd.Series(gdp_data, dtype=float)

# Fetch GDP data for the US and Europe
us_gdp = fetch_gdp_data("USA")
europe_gdp = fetch_gdp_data("EMU")  # Euro Area

# Combine into a DataFrame
gdp_df = pd.DataFrame({"US GDP": us_gdp, "Europe GDP": europe_gdp})
gdp_df.sort_index(inplace=True)  # Sort by year

# Plot GDP trends
plt.figure(figsize=(10, 6))
plt.plot(gdp_df.index, gdp_df["US GDP"], label="US GDP", marker="o")
plt.plot(gdp_df.index, gdp_df["Europe GDP"], label="Europe GDP", marker="s")

# Formatting the chart
plt.xlabel("Year")
plt.ylabel("GDP (in current USD)")
plt.title("US vs. Europe GDP (1945-Present)")
plt.legend()
plt.grid(True)
plt.show()
