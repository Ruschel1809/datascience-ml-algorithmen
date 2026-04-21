# Daten für die Analyse runterladen bei kaggle
# import kagglehub
#
# # Download latest version
# path = kagglehub.dataset_download("vjchoudhary7/customer-segmentation-tutorial-in-python")
#
# print("Path to dataset files:", path)

# Schritt 1 Datan bereinigen, dazu herausfinden, ob die Daten mehr als 5% fehlende WErte haben

import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Mall_Customers.csv")
# print(df.to_string())
#
# # Fehlende Werte in Prozent pro Spalte -> das isnull().mean() gibt den anteil NaN pro Spalte - multipliziert mit 100 ergibt das den Prozentsatz
# missing_percent = df.isnull().mean() * 100
#
# # Spalten mit mehr als 5% fehlenden Werten anzeigen
# print(missing_percent[missing_percent > 5])

# fehlende Werte visualisieren
# 1. Missingno (matplotlib wird benötigt, aber das ist meist eh installiert)
# import missingno as msno
# import matplotlib.pyplot as plt
#
# # einfache Matrixansicht
# msno.matrix(df)
#
# # Bar-Plot: Wie viele Wete fehlen pro Spalte
# msno.bar(df)
# plt.show()
#
# # Heatmap: Gibt Hinweise auf Zusammenhang zwischen fehlenden Werten
# msno.heatmap(df)
# plt.show()

# # fehlende Werte visualisieren
# # 2. Seaborn / Matplotlib
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# missing = df.isnull().sum()
# missing = missing[missing > 0]
#
# sns.barplot(x=missing.values, y=missing.index)
# plt.xlabel("Anzahl fehlender Werte")
# plt.ylabel("Spalten")
# plt.title("Fehlende Werte pro Spalte")
# plt.show()

# generelle Analyse eines unbekannten Datensatzes
# 1. erste Sichtung:
# df.shape           # Zeilen & Spalten
# df.columns         # Spaltennamen
# df.info()          # Datentypen & Null-Werte
# df.head()          # Vorschau

# 2. Überblick über fehlende Werte
# df.isnull().sum()           # Anzahl fehlender Werte pro Spalte
# df.isnull().mean()*100      # Prozentuale Anteile

# 3. Datentyp-Analyse
# Sind alle numerischen Werte auch als numerisch erkannt (float, int)
#
# Gibt es Text, der kategorisch ist und in object steckt
#
# Möglicherweise Datumswerte als Strings -> pd.to_datetime()

# 4. statische Grundanalyse
# df.describe()       # Nur für numerische Spalten
# df.describe(include='object')   # Für kategoriale
# df.nunique()        # Wie viele eindeutige Werte pro Spalte

# 5. Duplikate, Ausreißer, Ungereimtheiten
# df.duplicated().sum()

# Für ausreißer:
# sns.boxplot(x=df['deine_numerische_spalte'])

# 6. Zielspalte (falls supervised learning)
# Verteilung prüfen
# df['Ziel'].value_counts(normalize=True)

# Nur die zwei gewünschten Features auswählen
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

#erste visualisierung
plt.figure(figsize=(8, 5))
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c='gray')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Kunden ohne Cluster')
plt.grid(True)
plt.show()

# Elbow-Methode zur Bestimmung der optimalen Clusterzahl
inertia = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i, random_state=42).fit(X) # random_state für Reproduzierbarkeit der Ergebnisse; 42, weil es lustig ist
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(range(1,11), inertia, 'bo-') # Das erzeugt: Blaue Punkte (o) an den Werten von inertia, Linie (-) zwischen den Punkten, Blaue Farbe (b)
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Inertia')
plt.title('Elbow-Methode')
plt.grid(True)
plt.show()

# k=5 (aus Elbow-Methode Diagramm)
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# Visualisierung der Cluster
plt.figure(figsize=(8, 5))

# 1. Datenpunkte Zeichnen
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'],
            c=df['Cluster'], cmap='viridis', s=50)

# 2. Cluster-Zentren zeichnen
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Zentren')

# 3. Achsen und Titel
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('KMeans Cluster (k=5)')
plt.legend()
plt.grid(True)
plt.show()

# Silhouetten-Koeffizient
score2 = silhouette_score(X, df['Cluster'])
print(f"Silhouette Score 2 Features: {score2:.3f}")

# für verschiede k ausprobieren
scores = []
k_range = range(2, 11)  # wichtig: ab 2 (1 Cluster macht keinen Sinn!)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X)
    score = silhouette_score(X, labels)
    scores.append(score)

plt.plot(k_range, scores, 'bo-')
plt.xlabel("Anzahl der Cluster (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette-Analyse zur Bestimmung der optimalen Cluster-Anzahl")
plt.grid(True)
plt.show()

# Drei Features: 'Age', 'Annual Income (k$)', 'Spending Score (1-100)'
X3 = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standardisieren – wichtig bei KMeans!
scaler = StandardScaler() # Skaliert alle numerischen Features auf Standard-Normalverteilung: Mittelwert = 0, Standardabweichung = 1 -> jedes Feature wird in den gleichen Maßstab gebracht, egal ob Alter, Einkommen oder Punkte. Damit ein Feature, das sehr hohe Zahlenwerte hat das Cluster nicht dominiert, da es beim K-Means um Abstände geht.
X3_scaled = scaler.fit_transform(X3)

# Elbow erneut bestimmen
inertia = []
for i in range(1,16):
    kmeans = KMeans(n_clusters=i, random_state=42).fit(X3_scaled) # random_state für Reproduzierbarkeit der Ergebnisse; 42, weil es lustig ist
    inertia.append(kmeans.inertia_)
plt.plot(range(1,16), inertia, 'bo-') # Das erzeugt: Blaue Punkte (o) an den Werten von inertia, Linie (-) zwischen den Punkten, Blaue Farbe (b)
plt.xlabel('Anzahl der Cluster')
plt.ylabel('Inertia')
plt.title('Elbow-Methode')
plt.grid(True)
plt.show()

# Clustering erneut anwenden
# KMeans mit den 3 Features
kmeans3 = KMeans(n_clusters=6, random_state=42)
df['Cluster3D'] = kmeans3.fit_predict(X3_scaled)

#3D Visualisierung
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Age'], df['Annual Income (k$)'], df['Spending Score (1-100)'],
           c=df['Cluster3D'], cmap='viridis', s=60)

ax.set_xlabel('Age')
ax.set_ylabel('Annual Income (k$)')
ax.set_zlabel('Spending Score (1-100)')
ax.set_title('KMeans Clustering mit 3 Features')

plt.show()

# Silhouetten-Koeffizient
score = silhouette_score(X3_scaled, df['Cluster3D'])
print(f"Silhouette Score: {score:.3f}")

# für verschiede k ausprobieren
scores = []
k_range = range(2, 16)  # wichtig: ab 2 (1 Cluster macht keinen Sinn!)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X3_scaled)
    score = silhouette_score(X3_scaled, labels)
    scores.append(score)

plt.plot(k_range, scores, 'bo-')
plt.xlabel("Anzahl der Cluster (k)")
plt.ylabel("Silhouette Score")
plt.title("Silhouette-Analyse zur Bestimmung der optimalen Cluster-Anzahl")
plt.grid(True)
plt.show()