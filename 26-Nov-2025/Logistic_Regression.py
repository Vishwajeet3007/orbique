import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# ---- Create Synthetic Data ----
np.random.seed(0)
n = 200
X = np.random.randn(n, 2)
y = (X[:, 0] + X[:, 1] * 0.5 > 0).astype(int)

# ---- Train Logistic Regression ----
model = LogisticRegression()
model.fit(X, y)

# ---- Model Results ----
print("Accuracy:", model.score(X, y))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# ---- Plot Data + Decision Boundary ----
plt.figure(figsize=(7, 5))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="bwr", alpha=0.7)

# Decision boundary line
xx = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
yy = -(model.coef_[0][0] * xx + model.intercept_[0]) / model.coef_[0][1]

plt.plot(xx, yy, 'k--', label="Decision Boundary")
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
