import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression

# Data for Quality, Rate, and Cost
quality = np.array([10, 15, 20, 5, 8])
rate = np.array([5, 3, 2, 10, 8])
cost = np.array([50, 45, 40, 50, 64])

# Reshape data for linear regression
X = np.column_stack((rate, cost))  # Independent variables (Rate, Cost)
y = quality  # Dependent variable (Quality)

# Initialize and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients and intercept
intercept = model.intercept_
coefficients = model.coef_

# Print the results
print(f"Intercept: {intercept}")
print(f"Coefficients: {coefficients}")

# Create a grid for plotting the regression surface
rate_range = np.linspace(min(rate), max(rate), 100)
cost_range = np.linspace(min(cost), max(cost), 100)
rate_grid, cost_grid = np.meshgrid(rate_range, cost_range)
predicted_quality = model.predict(np.column_stack((rate_grid.ravel(), cost_grid.ravel()))).reshape(rate_grid.shape)

# Plotting 3D scatter plot and regression plane
fig = plt.figure(figsize=(10, 6))

# 3D scatter plot
ax = fig.add_subplot(121, projection='3d')
ax.scatter(rate, cost, quality, color='blue', label='Data points')
ax.set_xlabel('Rate')
ax.set_ylabel('Cost')
ax.set_zlabel('Quality')
ax.set_title('3D Scatter plot')

# 3D surface plot (regression plane)
ax = fig.add_subplot(122, projection='3d')
ax.plot_surface(rate_grid, cost_grid, predicted_quality, cmap='viridis', alpha=0.6)
ax.scatter(rate, cost, quality, color='red', label='Data points')
ax.set_xlabel('Rate')
ax.set_ylabel('Cost')
ax.set_zlabel('Quality')
ax.set_title('Regression Plane')

plt.tight_layout()
plt.show()

