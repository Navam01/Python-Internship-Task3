# Task 3 - Evaluate and Make Predictions

## 📌 Objective

The objective of this task is to evaluate the performance of the trained Linear Regression model and use it to predict exam scores for new study hours.

---

## 📂 Dataset

The dataset contains two columns:

| Hours Studied | Exam Score |
|--------------:|-----------:|
| 1 | 35 |
| 2 | 45 |
| 3 | 48 |
| 4 | 52 |
| 5 | 60 |
| 6 | 68 |
| 7 | 75 |
| 8 | 82 |
| 9 | 88 |
| 10 | 95 |

- **Feature (X):** Hours Studied
- **Target (y):** Exam Score

---

## 🛠 Technologies Used

- Python 3
- Pandas
- Scikit-learn

---

## 📚 Steps Performed

1. Imported the required libraries.
2. Used the trained Linear Regression model.
3. Predicted exam scores for the test dataset.
4. Calculated the Mean Absolute Error (MAE).
5. Compared actual and predicted scores.
6. Predicted the score for a student who studied **4.5 hours**.

---

## ▶️ Run the Program

```bash
python task3_evaluate_predictions.py
```

---

## 📊 Sample Output

```text
Mean Absolute Error: 2.15 points

   Actual  Predicted
0      88      86.75
1      45      47.20

Predicted score for 4.5 hours: 58.60
```

> **Note:** The exact values may vary slightly depending on the train-test split.

---

## 📖 Evaluation Metric

### Mean Absolute Error (MAE)

Mean Absolute Error measures the average difference between the actual values and the predicted values.

- Lower MAE indicates better model performance.
- An MAE close to **0** means the model is making highly accurate predictions.

Formula:

```
MAE = (|Actual - Predicted|) / Number of Samples
```

---

## 🔍 Prediction

The trained model predicts the exam score for a student studying **4.5 hours**.

Example:

```
Hours Studied : 4.5
Predicted Score : 58.60
```

---

## 📁 Project Structure

```
Task3_Evaluate_and_Predict/
│── task3_evaluate_predictions.py
└── README.md
```

---

## 🎯 Learning Outcomes

After completing this task, I learned how to:

- Evaluate a Machine Learning model.
- Calculate Mean Absolute Error (MAE).
- Compare predicted values with actual values.
- Use a trained model to make predictions for new data.

---

## 🚀 Future Improvements

- Use a larger dataset.
- Visualize prediction results using graphs.
- Evaluate additional metrics such as Mean Squared Error (MSE) and R² Score.
- Experiment with different regression algorithms.

---

## 👨‍💻 Author

**Your Name**

Machine Learning Internship
