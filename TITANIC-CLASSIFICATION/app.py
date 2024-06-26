import seaborn as sns

# Load Titanic dataset from Seaborn
titanic = sns.load_dataset('titanic')

# Display first few rows of the dataset to understand its structure
print(titanic.head())

# Check for missing values
print(titanic.isnull().sum())

# Handle missing values
titanic['age'].fillna(titanic['age'].median(), inplace=True)
titanic['embarked'].fillna(titanic['embarked'].mode()[0], inplace=True)

# Encode categorical variables
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
titanic['sex'] = encoder.fit_transform(titanic['sex'])
titanic['embarked'] = encoder.fit_transform(titanic['embarked'])

# Select relevant features
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
X = titanic[features]
y = titanic['survived']

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Random Forest Classifier
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict survival on the test set
y_pred = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

importances = model.feature_importances_

# Display feature importance
feature_importance = dict(zip(features, importances))
sorted_importance = sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)
for feature, importance in sorted_importance:
    print(f"{feature}: {importance:.4f}")
