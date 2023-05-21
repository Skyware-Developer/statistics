import pandas as pd

# Read the CSV file
df = pd.read_csv('game.csv')

# Define CPU prices (CPU: Price)
cpu_prices = {
    'CPU1': 99.03,
    'CPU2': 160.99,
    'CPU3': 548.03
}

# Calculate average FPS for each CPU
avg_fps = df.groupby('CPU')['FPS'].mean()

# Calculate FPS/Price ratio for each CPU
fps_price_ratio = avg_fps / avg_fps.index.map(cpu_prices)

# Create a DataFrame with the results
result_df = pd.DataFrame({'Average FPS': avg_fps, 'FPS/Price Ratio': fps_price_ratio})

# Print the results
print(result_df)
