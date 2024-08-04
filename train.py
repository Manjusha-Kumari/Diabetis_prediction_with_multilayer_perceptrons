from preprocessing import load_and_preprocess_data
from model import build_model
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve
import numpy as np
import joblib


# Load and preprocess data
file_path = "diabetes.csv"
X_train, X_val, X_test, y_train, y_val, y_test = load_and_preprocess_data(file_path)

# Build and train model
input_dim = X_train.shape[1]
model = build_model(input_dim)
model.fit(X_train, y_train, epochs=200, validation_data=(X_val, y_val))

# Evaluate model
train_scores = model.evaluate(X_train, y_train)
print("Training Accuracy: %.2f%%\n" % (train_scores[1] * 100))

test_scores = model.evaluate(X_test, y_test)
print("Testing Accuracy: %.2f%%\n" % (test_scores[1] * 100))

# Confusion matrix
y_test_pred = (model.predict(X_test) > 0.5).astype("int32")
c_matrix = confusion_matrix(y_test, y_test_pred)
ax = sns.heatmap(c_matrix, annot=True, xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'], cbar=False, cmap='Blues')
ax.set_xlabel("Prediction")
ax.set_ylabel("Actual")
plt.show()

# ROC Curve
y_test_pred_probs = model.predict(X_test)
FPR, TPR, _ = roc_curve(y_test, y_test_pred_probs)
plt.plot(FPR, TPR)
plt.plot([0, 1], [0, 1], '--', color='black')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
# Assuming 'model' is your trained model
joblib.dump(model, 'diabetes-prediction-api/diabetes_model.pkl')
