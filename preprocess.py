import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load dataset with error handling
try:
    data = pd.read_csv(r"C:\Users\DELL\Documents\extension\backend\Cleaned_Phishing_Dataset.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

# Check for non-numeric data and encode if necessary
non_numeric_cols = data.select_dtypes(include=['object']).columns

if len(non_numeric_cols) > 0:
    print(f"Non-numeric columns detected: {non_numeric_cols}")
    label_encoder = LabelEncoder()
    for col in non_numeric_cols:
        if col != 'label':  # Ensure label is not encoded
            data[col] = label_encoder.fit_transform(data[col].astype(str))
    print("Non-numeric columns encoded.")

# Features and Labels
if 'label' not in data.columns:
    print("Error: 'label' column not found in the dataset.")
    exit()

X = data.drop(columns=['label', 'FILENAME', 'URL'], errors='ignore')
y = data['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
print("Training the model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training completed.")

# Evaluate the model
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
try:
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved as model.pkl.")
except Exception as e:
    print(f"Error saving model: {e}")
