# Step 1: Setting up the environment
# pip install pandas sklearn matplotlib

# Step 2: Prepare the dataset
# Load the dataset
import pandas as pd

# TODO: make sure to replace 'cdss/diabetes_data.csv' with the actual path to your dataset
data = pd.read_csv('diabetes_data.csv')

# Step 3: Check the dataset
# Display the first few rows of the dataset
print(data.head())

# Summary statistics
print(data.describe())

# Check for missing values
print(data.isnull().sum())

# Step 4: Data Preprocessing
from sklearn.model_selection import train_test_split

X = data.drop('Outcome', axis=1)
y = data['Outcome']

# TODO: Split the dataset into training and testing sets with a 70-30 split (test_size=0.3)
data_train, data_test = train_test_split(data, test_size=0.3, random_state=42)
X_train = data_train.drop('Outcome', axis=1)
y_train = data_train['Outcome']
X_test = data_test.drop('Outcome', axis=1)
y_test = data_test['Outcome']

# Step 5: Model Building
from sklearn.linear_model import LogisticRegression

# TODO: Create a Logistic Regression model and fit it on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Model Evaluation
from sklearn.metrics import accuracy_score

# TODO: Use the model to make predictions on the test data
y_pred = model.predict(X_test)

# TODO: Call the accuracy_score function to calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")