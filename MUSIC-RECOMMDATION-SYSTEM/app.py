import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Load the dataset
data = pd.read_csv('user_song_data.csv')

# Example dataset structure:
# user_id, song_id, timestamp, repeated_play_within_month
# 1, 101, 2023-01-01 10:00:00, 1
# 2, 102, 2023-01-02 12:00:00, 0

# Convert timestamp to datetime
data['timestamp'] = pd.to_datetime(data['timestamp'])

# Generate some example features
data['hour'] = data['timestamp'].dt.hour
data['dayofweek'] = data['timestamp'].dt.dayofweek

# Aggregate features by user and song
features = data.groupby(['user_id', 'song_id']).agg({
    'timestamp': ['count'],
    'hour': ['mean'],
    'dayofweek': ['mean']
}).reset_index()

# Flatten multi-level columns
features.columns = ['user_id', 'song_id', 'play_count', 'avg_hour', 'avg_dayofweek']

# Merge with the original data to get the labels
data = data.merge(features, on=['user_id', 'song_id'])
data = data.drop_duplicates(subset=['user_id', 'song_id'])

# Select features and labels
X = data[['play_count', 'avg_hour', 'avg_dayofweek']]
y = data['repeated_play_within_month']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)

print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')
print(f'ROC AUC Score: {roc_auc:.2f}')

# Generate predictions for a new user-song pair
new_data = pd.DataFrame({
    'play_count': [5],
    'avg_hour': [14],
    'avg_dayofweek': [3]
})

# Standardize the new data
new_data = scaler.transform(new_data)

# Predict the likelihood of repeated play
predicted_proba = model.predict_proba(new_data)[:, 1]
print(f'Predicted probability of repeated play: {predicted_proba[0]:.2f}')
