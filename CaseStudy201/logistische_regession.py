import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score

# 2. Daten einlesen
df = pd.read_csv("K4.0026_2.C.01_Salaries")

# Erste Datenanalyse und Visualisierung
# Daten anzeigen
print(df.head())

# Scatterplot: Level vs Salary
plt.scatter(df['Level'], df['Salary'], color='blue')
plt.title("Gehalt nach Level")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.grid(True)
plt.show()


# 4. Daten bereinigen
# Duplikate entfernen
df = df.drop_duplicates()

# Gehälter über 500000 entfernen (Ausreißer wie CEO)
df = df[df['Salary'] < 500000]

# 5. Lineare Regression
# X und y vorbereiten
X = df[['Level']]
y = df['Salary']

# Modell erstellen und trainieren
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Vorhersage
y_pred = lin_reg.predict(X)

# Plot
plt.scatter(X, y, color='gray')
plt.plot(X, y_pred, color='red', linewidth=2)
plt.title("Lineare Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# R²-Wert
print(f"R² (lineare Regression): {r2_score(y, y_pred):.4f}")

# 6. Polynomiale Regression (z.B. Grad 4)
# Polynom-Features erstellen
degree = 4
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(X)

# Modell trainieren
poly_reg = LinearRegression()
poly_reg.fit(X_poly, y)

# Vorhersage
y_poly_pred = poly_reg.predict(X_poly)

# Plot
plt.scatter(X, y, color='gray')
plt.plot(X, y_poly_pred, color='green', linewidth=2)
plt.title(f"Polynomiale Regression (Grad {degree})")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# R²-Wert
print(f"R² (Polynom-Regression, Grad {degree}): {r2_score(y, y_poly_pred):.4f}")

# 7. Beide Modelle im Vergleich
plt.scatter(X, y, color='gray', label='Daten')
plt.plot(X, y_pred, color='red', label='Linear')
plt.plot(X, y_poly_pred, color='green', label=f'Polynom Grad {degree}')
plt.title("Vergleich: Linear vs. Polynom")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.legend()
plt.grid(True)
plt.show()

# 8. Beispiel: Gehalt für Level 6.5 vorhersagen
level_input = np.array([[6.5]])
level_input_poly = poly.transform(level_input)
predicted_salary = poly_reg.predict(level_input_poly)

print(f"Vorhergesagtes Gehalt für Level 6.5: {predicted_salary[0]:.2f} €")