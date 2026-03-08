import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv("solar_data.csv")

# Display basic data
print("Station Data:")
print(data)

# Calculate average energy per panel
data['Average_Energy'] = data['Daily_Energy_kWh']
print("\nAverage energy per panel:")
print(data[['Panel_ID','Average_Energy']])

# Find panel with highest energy
max_panel = data.loc[data['Daily_Energy_kWh'].idxmax()]
print(f"\nHighest energy: {max_panel['Panel_ID']} → {max_panel['Daily_Energy_kWh']} kWh")

# Find panel with lowest energy
min_panel = data.loc[data['Daily_Energy_kWh'].idxmin()]
print(f"Lowest energy: {min_panel['Panel_ID']} → {min_panel['Daily_Energy_kWh']} kWh")

# Visualization 1: Daily energy output per panel
plt.figure(figsize=(8,5))
plt.bar(data['Panel_ID'], data['Daily_Energy_kWh'], color='orange')
plt.title("Daily Energy Output per Solar Panel")
plt.xlabel("Panel ID")
plt.ylabel("Energy (kWh)")
plt.grid(axis='y')
plt.savefig("energy_bar_chart.png") 
plt.show()

# Visualization 2: Effect of dust on energy production
plt.figure(figsize=(8,5))
plt.scatter(data['Dust_Level_Percent'], data['Daily_Energy_kWh'], color='blue')
plt.title("Effect of Dust on Energy Production")
plt.xlabel("Dust Level (%)")
plt.ylabel("Energy (kWh)")
plt.grid(True)
plt.savefig("dust_vs_energy.png") 
plt.show()

print("\nSuccess: Images 'energy_bar_chart.png' and 'dust_vs_energy.png' have been generated.")

