import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.svm import SVC

# Datei einlesen
df = pd.read_csv('K4.0026_2.C.02_MobilePhone.csv')

price_mapping = {
    'l': 'Low',
    'm': 'Medium',
    'h': 'High'
}
df['Price Range'] = df['Price Range'].map(price_mapping)

# --------- 3. Scatter-Plots ----------

# Plot 1: Battery Power vs Internal Memory
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='battery_power', y='int_memory', hue='Price Range', palette='Set1')
plt.title("Battery Power vs Internal Memory")
plt.xlabel("Battery Power")
plt.ylabel("Internal Memory (GB)")
plt.legend()
plt.show()

# Plot 2: Frontkamera-Megapixel vs Bluetooth
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='frontcamermegapixels', y='blue', hue='Price Range', palette='Set2')
plt.title("Frontkamera-Megapixel vs Bluetooth")
plt.xlabel("Frontkamera (MP)")
plt.ylabel("Bluetooth (0 = No, 1 = Yes)")
plt.yticks([0, 1])
plt.show()

# Plot 3: Internal Memory vs Frontkamera-Megapixel
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='int_memory', y='frontcamermegapixels', hue='Price Range', palette='Set3')
plt.title("Internal Memory vs Frontkamera-Megapixel")
plt.xlabel("Internal Memory (GB)")
plt.ylabel("Frontkamera (MP)")
plt.show()

# Plot 4: 3D Scatter-Plot
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')
colors = {'Low': 'blue', 'Medium': 'orange', 'High': 'green'}
ax.scatter(
    df['battery_power'],
    df['blue'],
    df['frontcamermegapixels'],
    c=df['Price Range'].map(colors),
    label=df['Price Range']
)
ax.set_xlabel("Battery Power")
ax.set_ylabel("Bluetooth (0/1)")
ax.set_zlabel("Frontkamera (MP)")
plt.title("3D Scatter-Plot: Battery Power, Bluetooth, Frontkamera")
plt.show()

# Optional: Mapping von 'l', 'm', 'h' zu 'Low', 'Medium', 'High'
price_mapping = {'l': 'Low', 'm': 'Medium', 'h': 'High'}
df['Price Range'] = df['Price Range'].map(price_mapping)

# Nur relevante Features auswählen
X = df[['battery_power', 'fc']]  # Features
y = df['Price Range']            # Zielvariable

# Zielvariable (Strings) in Zahlen umwandeln
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)  # z.B. Low → 0, Medium → 1, High → 2

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Umwandlung zurück in 'Low', 'Medium', 'High' zur besseren Lesbarkeit
y_test_labels = label_encoder.inverse_transform(y_test)
y_pred_labels = label_encoder.inverse_transform(y_pred)

# Ergebnisbewertung
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test_labels, y_pred_labels))

models = {
    'Random Forest': RandomForestClassifier(),
    'Logistic Regression': LogisticRegression(),
    'KNN': KNeighborsClassifier(),
    'SVM': SVC()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    acc = model.score(X_test, y_test)
    print(f"{name}: {acc:.2f}")