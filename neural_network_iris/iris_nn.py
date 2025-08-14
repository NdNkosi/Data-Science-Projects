import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# 1. Load the Iris dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target

# 2. Normalize input values using Min-Max scaling
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split into training (60%), validation (20%), test (20%)
X_temp, X_test, y_temp, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)  # 0.25 * 0.8 = 0.2

# Confirm shape of splits
print("Train set:", X_train.shape, y_train.shape)
print("Validation set:", X_val.shape, y_val.shape)
print("Test set:", X_test.shape, y_test.shape)
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# 5. Build the neural network
model = MLPClassifier(
    hidden_layer_sizes=(20,10),  # one hidden layer with 20 nodes
    activation='relu',     # linear activation (approximates sum-of-squares loss)
    solver='sgd',              # gradient descent
    learning_rate_init=0.05,
    max_iter=1,                # train for 1 epoch at a time
    warm_start=True,
    shuffle=True,          # keep model weights between epochs
    random_state=42
)

EPOCHS = 300

for epoch in range(EPOCHS):
    model.fit(X_train, y_train)

    # Get predictions as class labels
    y_train_pred = model.predict(X_train)
    y_val_pred = model.predict(X_val)

    # Convert one-hot true labels to class indices
    y_train_true = y_train
    y_val_true = y_val


    # Compute losses using label arrays (1D)
    train_loss = mean_squared_error(y_train_true, y_train_pred) * len(y_train_true)
    val_loss = mean_squared_error(y_val_true, y_val_pred) * len(y_val_true)

    print(f"Epoch {epoch+1}: Train Loss = {train_loss:.4f}, Validation Loss = {val_loss:.4f}")


# 6. After training, evaluate on test set
y_test_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score
import numpy as np

# Convert one-hot back to class indices
y_test_pred = model.predict(X_test)
y_test_true = y_test
test_accuracy = accuracy_score(y_test_true, y_test_pred)

print(f"\nTest Set Accuracy: {test_accuracy:.2%}")

