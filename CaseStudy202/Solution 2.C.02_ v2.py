# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("MobilePhone.csv")

# Convert price_range to numeric if needed
price_map = {"low": 0, "medium": 1, "high": 2}
df['price_range_numeric'] = df['price_range'].map(price_map)

# Select features (more than original)
features = ['battery_power', 'front_camera_megapixels', 'int_memory', 'blue', 'dual_sim']
X = df[features]
y = df['price_range_numeric']

# Split data randomly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Scale features (important for distance-based models, optional for RandomForest)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Test classifier
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)

# Optional: inspect feature importance
importances = clf.feature_importances_
for feat, imp in zip(features, importances):
    print(f"{feat}: {imp:.2f}")
# Bibliotheken importieren
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ==========================
# Änderungen zur Verbesserung der Genauigkeit:
# 1. Mehr Features verwenden:
#    - Original: nur 'battery_power' und 'front_camera_megapixels'
#    - Neu: 'battery_power', 'front_camera_megapixels', 'int_memory', 'blue', 'dual_sim'
#      -> Mehr Informationen für die Klassifikation
# 2. Korrekte Kodierung kategorialer Features:
#    - 'blue' und 'dual_sim' sind bereits 0/1 (binär)
#    - 'price_range' wird zu numerisch: low=0, medium=1, high=2
# 3. Feature-Skalierung:
#    - StandardScaler normalisiert die Werte
#    - Wichtig für distanzbasierte Modelle wie KNN, optional für RandomForest
# 4. Stärkerer Klassifikator:
#    - RandomForestClassifier kann nicht-lineare Zusammenhänge erfassen
# 5. Zufällige Datenaufteilung:
#    - Vermeidet Verzerrungen, besser als einfache 80/20-Aufteilung am Anfang
# ==========================

# Daten laden
df = pd.read_csv("MobilePhone.csv")

# Price Range in numerische Werte umwandeln
price_map = {"low": 0, "medium": 1, "high": 2}
df['price_range_numeric'] = df['price_range'].map(price_map)

# Features auswählen (mehr als im Original)
features = ['battery_power', 'front_camera_megapixels', 'int_memory', 'blue', 'dual_sim']
X = df[features]
y = df['price_range_numeric']

# Daten zufällig in Trainings- und Testdaten aufteilen
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Feature-Skalierung (Standardisierung)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Klassifikator trainieren (RandomForest)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_scaled, y_train)

# Modell testen und Genauigkeit berechnen
y_pred = clf.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print("Testgenauigkeit:", accuracy)

# Optional: Feature-Wichtigkeit anzeigen
importances = clf.feature_importances_
for feat, imp in zip(features, importances):
    print(f"{feat}: {imp:.2f}")
