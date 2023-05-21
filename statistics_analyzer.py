import pandas as pd

# Read the CSV file
df = pd.read_csv('game.csv')

# Check the dimensions of the data
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

# Summary statistics of numerical columns
print(df.describe())

# Count of unique values in each column
print(df.nunique())

# Group by 'Game' column and calculate average FPS
avg_fps_by_game = df.groupby('Game')['FPS'].mean()
print(avg_fps_by_game)

# Sort data by 'FPS' column in descending order
sorted_data = df.sort_values('FPS', ascending=False)
print(sorted_data.head())

# Filter data for games released after 2015
filtered_data = df[df['Year'] > 2015]
print(filtered_data.head())

