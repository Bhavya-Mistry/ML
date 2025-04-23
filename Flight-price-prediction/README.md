# ✈️ Flight Price Prediction

This project aims to predict the flight prices based on various features using machine learning models, including Linear Regression and Decision Tree Regression. The dataset used contains information about flight details such as airline, source, destination, duration, stops, and additional features.

## Project Structure

- **`Untitled3.ipynb`**: Jupyter Notebook containing the full code for data processing, feature engineering, model training, and evaluation.
- **`Flight-price-predication.xlsx`**: Dataset used for training and testing the models.

## Libraries Used

- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical operations.
- **sklearn**: Machine learning algorithms and tools for training, evaluation, and grid search.
- **seaborn**: Visualization library for statistical data.
- **matplotlib**: Visualization library for creating static, animated, and interactive visualizations in Python.

## Dataset

The dataset contains the following features:

- **Airline**: The airline operating the flight.
- **Source**: The source city from which the flight departs.
- **Destination**: The destination city of the flight.
- **Total_Stops**: The total number of stops in the flight.
- **Additional_Info**: Additional details like flight class, baggage, etc.
- **Duration**: Duration of the flight in hours and minutes.
- **Price**: The price of the flight (target variable).

## Steps in the Notebook

### 1. Load Dataset
The dataset is loaded from an Excel file using `pandas`.

### 2. Feature Engineering
- **Date_of_Journey**: Extracts the day of the week and creates a new feature indicating whether it's a weekday or weekend.
- **Duration**: Converts the duration from string format to minutes.
- **One-Hot Encoding**: Encodes categorical features such as airline, source, destination, total stops, and additional info using one-hot encoding.
- **Handling Missing Data**: Removes rows with missing values.

### 3. Train-Test Split
The dataset is split into training and testing datasets using an 80-20 split ratio.

### 4. Feature Scaling
Standard scaling is applied to the features to improve the performance of machine learning algorithms.

### 5. Model Training

#### Linear Regression
- The Linear Regression model is trained on the scaled training data and evaluated using the testing data. The following evaluation metrics are used:
  - **R² Score**: Proportion of variance in the dependent variable that is predictable from the independent variables.
  - **Mean Absolute Error (MAE)**: The average of the absolute errors between predicted and actual values.
  - **Mean Squared Error (MSE)**: The average of the squared errors between predicted and actual values.
  - **Root Mean Squared Error (RMSE)**: The square root of MSE.
  - **Mean Absolute Percentage Error (MAPE)**: The average of absolute percentage errors between predicted and actual values.

#### Decision Tree Regressor
- A Decision Tree Regressor model is also trained using a GridSearchCV to find the best hyperparameters, including:
  - **max_depth**: Maximum depth of the tree.
  - **min_samples_split**: The minimum number of samples required to split an internal node.
  - **min_samples_leaf**: The minimum number of samples required to be at a leaf node.
  - **max_features**: The number of features to consider when looking for the best split.

### 6. Model Evaluation
- Both models are evaluated using the metrics mentioned above. The best parameters for the Decision Tree model are selected based on cross-validation results.

### Linear Regression

- **R² Score**: 69.93
- **MAE**: 1708.24
- **MSE**: 5547602.32
- **RMSE**: 2355.33
- **MAPE**: 20.88 #

### Decision Tree

- **R² Score**: 73.00
- **MAE**: 1442.08
- **MSE**: 4982188.27
- **RMSE**: 2232.08
- **MAPE**: 16.94 %



## Conclusion

This project demonstrates the power of machine learning for predicting flight prices. You can experiment with different machine learning models, feature engineering techniques, and hyperparameters to improve the predictions.

---

### How to Run the Project

1. Install the required libraries by running:
   ```bash
   pip install -r requirements.txt
