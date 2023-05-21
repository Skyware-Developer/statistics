import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_csv('game.csv')

# Define CPU prices (CPU: Price)
cpu_prices = {
    'CPU1': 99.03,
    'CPU2': 160.99,
    'CPU3': 548.03
}

# Create a new column 'Price' in the DataFrame based on the CPU prices
df['Price'] = df['CPU'].map(cpu_prices)

# Define the feature (price) and target (FPS) variables
X = df['Price'].values.reshape(-1, 1)
y = df['FPS'].values

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Get the coefficients (slope and intercept)
slope = model.coef_[0]
intercept = model.intercept_

# Predict FPS based on a range of prices
min_price = min(cpu_prices.values())
max_price = max(cpu_prices.values())
prices = np.linspace(min_price, max_price, num=100)
predicted_fps = model.predict(prices.reshape(-1, 1))

# Plot the data and the linear regression line
plt.scatter(X, y, color='blue', label='Data')
plt.plot(prices, predicted_fps, color='red', label='Linear Regression')
plt.xlabel('Price')
plt.ylabel('FPS')
plt.title('Linear Regression: FPS vs Price')
plt.legend()
plt.show()
