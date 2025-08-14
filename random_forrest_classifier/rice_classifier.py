from scipy.io import arff
import pandas as pd

# Load the data and metadata
data, meta = arff.loadarff('Rice_Cammeo_Osmancik.arff')

# Convert the structured NumPy array to a DataFrame
df = pd.DataFrame(data)

# Decode byte strings in the 'Class' column (optional)
df['Class'] = df['Class'].str.decode('utf-8')

# Split data
from sklearn.model_selection import train_test_split
X = df[['Area', 'Perimeter', 'Major_Axis_Length', 'Minor_Axis_Length', 'Eccentricity', 'Convex_Area', 'Extent']]
y = df['Class']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=104, test_size=0.25, shuffle=True)

# Train model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predicition
y_pred = model.predict(X_test)

# Evaluations
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
conf_matrix = confusion_matrix(y_test, y_pred)
acc_score = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary', pos_label='Cammeo')
recall = recall_score(y_test, y_pred, average='binary', pos_label='Cammeo')
f1 = f1_score(y_test, y_pred, average='binary', pos_label='Cammeo')
print('Confusion Matrix:\n', conf_matrix)
print('Accuracy Score:', acc_score)
print('Precision:', precision)
print('Recall:', recall)
print('F1 Score:', f1)
