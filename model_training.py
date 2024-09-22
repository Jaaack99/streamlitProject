import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load Titanic dataset from CSV
titanic = pd.read_csv('train.csv')

# Drop specified columns
titanic = titanic.drop(columns=['PassengerId', 'Name', 'SibSp', 'Ticket', 'Cabin'])

# Basic preprocessing
titanic = titanic.dropna(subset=['Age', 'Sex', 'Fare', 'Pclass', 'Embarked', 'Parch'])
le = LabelEncoder()
titanic['Sex'] = le.fit_transform(titanic['Sex'])
titanic['Pclass'] = le.fit_transform(titanic['Pclass'])
titanic['Embarked'] = le.fit_transform(titanic['Embarked'])

# Select features and target variable
X = titanic[['Sex', 'Age', 'Fare', 'Pclass', 'Parch']]
y = titanic['Survived']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the model to a file
joblib.dump(model, 'titanic_model.pkl')
print("Model saved to titanic_model.pkl")