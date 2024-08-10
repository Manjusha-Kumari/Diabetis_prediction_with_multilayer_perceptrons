import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, roc_curve

# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

# Load dataset
df = pd.read_csv("diabetes.csv")



# Plot histograms
df.hist(figsize=(10, 10))
plt.show()

# Density plots
plt.subplots(3, 3, figsize=(15, 15))
for idx, col in enumerate(df.columns):
    ax = plt.subplot(3, 3, idx + 1)
    sns.distplot(df[df.Outcome == 0][col], hist=False, label="No Diabetes", kde_kws={'linestyle': '-', 'color': 'black'})
    sns.distplot(df[df.Outcome == 1][col], hist=False, label="Diabetes", kde_kws={'linestyle': '--', 'color': 'black'})
    ax.set_title(col)
plt.subplot(3, 3, 9).set_visible(False)
plt.show()



# Replace 0 values with NaN
columns_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[columns_with_zeros] = df[columns_with_zeros].replace(0, np.nan)

# Fill NaN values with the mean of the column
df.fillna(df.mean(), inplace=True)



# Standardize data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.drop(columns=['Outcome']))
df_scaled = pd.DataFrame(df_scaled, columns=df.columns[:-1])
df_scaled['Outcome'] = df['Outcome']



# Separate features and target
X = df_scaled.drop(columns=['Outcome'])
y = df_scaled['Outcome']

# Split data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)



# Build the model
model = Sequential([
    Dense(32, activation='relu', input_dim=8),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=200, validation_data=(X_val, y_val))



# Evaluate on training data
train_loss, train_acc = model.evaluate(X_train, y_train)
print(f"Training Accuracy: {train_acc * 100:.2f}%")

# Evaluate on test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Testing Accuracy: {test_acc * 100:.2f}%")

# Confusion Matrix
y_test_pred = (model.predict(X_test) > 0.5).astype("int32")
c_matrix = confusion_matrix(y_test, y_test_pred)
sns.heatmap(c_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['No Diabetes', 'Diabetes'], yticklabels=['No Diabetes', 'Diabetes'])
plt.xlabel("Prediction")
plt.ylabel("Actual")
plt.show()

# ROC Curve
y_test_pred_probs = model.predict(X_test)
fpr, tpr, _ = roc_curve(y_test, y_test_pred_probs)
plt.plot(fpr, tpr, label='ROC Curve')
plt.plot([0, 1], [0, 1], 'k--')  # Diagonal line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()