SmartHealth Predictive Analyzer
SmartHealth Predictive Analyzer is a machine learning project that predicts the likelihood of diabetes based on a set of health metrics. The project uses advanced machine learning techniques, including Random Forest and Logistic Regression models, to predict whether an individual will develop diabetes based on their health-related data. The analysis includes data cleaning, feature engineering, model training, hyperparameter tuning, and model evaluation.

Table of Contents
Project Overview

Tech Stack

Installation

Data Description

Model Development

Data Preprocessing

Model Training

Model Evaluation

Results

Future Work

License

Project Overview
The objective of this project is to build a predictive model that can determine whether an individual is at risk of developing diabetes. Using historical data about patient health records, the model is trained to predict the Outcome (whether a person has diabetes) based on various features such as Glucose, BMI, Age, Blood Pressure, etc..

This project is designed to demonstrate the use of machine learning for healthcare predictions, and it is structured to help you understand the process from data collection to model deployment.

Tech Stack
Python 3.x

Libraries:

Pandas

NumPy

Matplotlib & Seaborn (for data visualization)

Scikit-learn (for machine learning models)

SciPy (for statistical analysis)

Jupyter Notebook (for interactive coding)

VS Code (for code editing)

Installation
To run the code on your local machine, follow these steps:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/Bhavya-Mistry/Data-Science.git
Navigate to the project folder:

bash
Copy
Edit
cd Data-Science/SmartHealth-Predictive-Analyzer
Install the required dependencies: You can install the required dependencies by running:

bash
Copy
Edit
pip install -r requirements.txt
Run the Jupyter notebook to start the analysis:

bash
Copy
Edit
jupyter notebook model.ipynb
Data Description
The dataset used for this analysis is a diabetes prediction dataset. It contains data about various health metrics of patients, including:


Column Name	Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration (mg/dL)
Blood Pressure	Diastolic blood pressure (mm Hg)
Skin Thickness	Triceps skin fold thickness (mm)
Insulin	2-hour serum insulin (mu U/ml)
BMI	Body mass index (kg/m^2)
Diabetes Pedigree Function	Diabetes pedigree function (a function of family history)
Age	Age (years)
Outcome	Class variable (1 if diabetic, 0 otherwise)
Model Development
Data Preprocessing
The data was first cleaned by performing the following steps:

Handling Missing Data: Null values were handled appropriately.

Outlier Detection: Outliers were detected using Z-scores and removed from the dataset to improve model accuracy.

Feature Scaling: Features were scaled using StandardScaler to normalize the range of the data.

Model Training
Two models were implemented:

Random Forest Classifier: A Random Forest model was trained with hyperparameter tuning using GridSearchCV to find the best-performing parameters.

Logistic Regression: A Logistic Regression model was also trained as a baseline for comparison.

Both models were evaluated using accuracy, precision, recall, and F1 score, and the confusion matrix was used to assess model performance.

Hyperparameter Tuning (Random Forest)
The Random Forest model underwent hyperparameter tuning with the following parameters:

n_estimators: Number of trees in the forest.

max_depth: Maximum depth of the trees.

min_samples_split: Minimum samples required to split a node.

min_samples_leaf: Minimum samples required to be at a leaf node.

Model Evaluation
The evaluation of the models was done using the following metrics:

Accuracy: The percentage of correctly classified instances.

Precision: The percentage of true positive predictions among all positive predictions.

Recall: The percentage of true positives among all actual positives.

F1 Score: The harmonic mean of precision and recall.

Results
The model performance is as follows:

Random Forest Classifier (Tuned):

Accuracy: 80%

Precision: 80%

Recall: 75%

F1-Score: 77%

Logistic Regression:

Accuracy: 78%

Precision: 76%

Recall: 74%

F1-Score: 75%

From the results, we can see that the Random Forest model performed slightly better than Logistic Regression, showing a higher accuracy and F1 score.

Confusion matrices for both models are provided to visualize the performance in terms of true positives, false positives, true negatives, and false negatives.

Future Work
Model Improvements: Experiment with other machine learning algorithms such as XGBoost or SVM to improve performance.

Hyperparameter Optimization: Further refine hyperparameters using advanced methods like RandomizedSearchCV or Bayesian Optimization.

Real-time Prediction: Implement real-time prediction using a web application or deploy the model as an API.

License
This project is open-source and available under the MIT License.
