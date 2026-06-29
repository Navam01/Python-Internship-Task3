import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Create dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 45, 48, 52, 60, 68, 75, 82, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Hours']]
y = df['Score']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict scores for the test data
y_pred = model.predict(X_test)

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

print("===== Model Evaluation =====")
print(f"Mean Absolute Error (MAE): {mae:.2f} points")

# Compare actual vs predicted values
results = pd.DataFrame({
    'Hours': X_test['Hours'].values,
    'Actual Score': y_test.values,
    'Predicted Score': y_pred.round(2)
})

print("\n===== Actual vs Predicted Scores =====")
print(results)

# Predict score for a new student
new_hours = [[4.5]]
predicted_score = model.predict(new_hours)

print("\n===== New Prediction =====")
print(f"Predicted score for 4.5 study hours: {predicted_score[0]:.2f}")