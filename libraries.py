# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean
numbers = np.arange(1, 11)
mean_value = np.mean(numbers)
print(f"Mean of numbers 1 to 10: {mean_value}")

# 2. Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 29],
    'Score': [88, 92, 95, 70, 85]
}
df = pd.DataFrame(data)
print("\nSummary statistics for the DataFrame:")
print(df.describe())

# 3. Fetch data from a public API using requests and print a key piece of information
response = requests.get('https://api.agify.io?name=michael')
if response.status_code == 200:
    data = response.json()
    print(f"\nPredicted age for the name 'Michael': {data.get('age')}")
else:
    print("Failed to fetch data from API")

# 4. Plot a simple line graph using matplotlib
plt.plot(numbers, numbers**2)  # Plotting y = x^2 for numbers 1 to 10
plt.title("Simple Line Graph: y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
