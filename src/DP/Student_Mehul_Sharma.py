import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample dataset
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable
y = np.array([2, 4, 5, 4, 5])  # Dependent variable

# Create and train model
model = LinearRegression()
model.fit(X, y)

# Get slope (m) and intercept (c)
m = model.coef_[0]
c = model.intercept_
print(f"Regression Equation: y = {m:.2f}x + {c:.2f}")

# Predictions
y_pred = model.predict(X)

# Plot data and regression line
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, y_pred, color='red', linewidth=2, label="Regression Line")
plt.xlabel("X (Independent Variable)")
plt.ylabel("y (Dependent Variable)")
plt.legend()
plt.show()
