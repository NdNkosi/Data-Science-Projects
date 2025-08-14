# Neural Network Classifier – Iris Dataset

**Tools:** Python, Scikit-learn  
**Dataset:** [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)

## 🎯 Objective
Build and train a feedforward neural network to classify iris flower species based on four input features.

## 🛠 Key Steps
1. **Data Preparation**
   - Min-max normalization of input features
   - One-hot encoding of target labels
2. **Model Architecture**
   - Input layer: 4 nodes
   - 1 hidden layer: 20 nodes
   - Output layer: 3 nodes
3. **Training**
   - Train/validation/test split
   - Sum-of-squares loss function
   - Monitored training & validation loss after each epoch
4. **Evaluation**
   - Accuracy on test set
   - Visual inspection of loss curve (optional)

## 📈 Results
- Achieved test accuracy: **95%+**
- Observed stable training and validation losses

## 📚 Skills Learned
- Data preprocessing with `scikit-learn`
- Building and evaluating neural network models
- Parameter tuning for better performance
