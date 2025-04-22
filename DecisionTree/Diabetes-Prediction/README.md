# 🩺 Diabetes Prediction using Decision Tree

This project uses the **Pima Indians Diabetes Dataset** and applies a **Decision Tree Classifier** to predict whether a patient has diabetes based on diagnostic measurements.

---

## 📊 Dataset

- Source: [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Rows: 768
- Columns: 9 (8 features + 1 target)

### Features:
- `Pregnancies`: Number of times pregnant
- `Glucose`: Plasma glucose concentration
- `BloodPressure`: Diastolic blood pressure (mm Hg)
- `SkinThickness`: Triceps skinfold thickness (mm)
- `Insulin`: 2-Hour serum insulin (mu U/ml)
- `BMI`: Body mass index
- `DiabetesPedigreeFunction`: Diabetes pedigree function
- `Age`: Age (years)

### Target:
- `Outcome`: 1 (diabetic), 0 (non-diabetic)

---

## 🧠 Model

- **Model Used**: `DecisionTreeClassifier` from `sklearn`
- **Train-Test Split**: 80% training / 20% testing
- **Performance Metric**: Accuracy

---

## 📈 Result

- ✅ Achieved accuracy: ~70-75% (varies slightly due to randomness in train-test split)
- ✅ Trained model visualized as a decision tree

---

## 🖼️ Visualization

The trained decision tree is saved as an image:

**`diabetes_tree.png`**

![Decision Tree](diabetes_tree.png)

---

## 🛠️ Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
