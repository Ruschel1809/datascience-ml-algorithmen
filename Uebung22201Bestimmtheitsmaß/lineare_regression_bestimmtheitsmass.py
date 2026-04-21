import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Hilfsfunktion: Erzeugt Polynomfeatures bis zu einem bestimmten Grad, wobei x eine Spalte mit Eingabedaten ist
def polynomial_features(X, grad):
    X_poly = np.ones((X.shape[0], 1))  # Neues Array für den Konstanten Anteil im Polynom: Spalte voller Einsen mit so vielen Zeilen wie X hat
    for d in range(1, grad + 1): # Schleifen, die für alle Grade von 1 bis grad läuft
        X_poly = np.hstack((X_poly, X**d)) # berechnet die Einträge aus X hoch d und fügt die Spalten zusammen
    return X_poly

# Hilfsfunktion: Teilt Daten in k Gruppen
def teile_in_k_gruppen(X, k):
    indices = np.arange(len(X)) # Array mit fortlaufenden Indizes
    np.random.shuffle(indices) # Indizes mischen, damit zufällig aufgeteilt wird
    gruppe_sizes = np.full(k, len(X) // k) # Array der Länge k, wobei jede "Gruppe" etwa gleich viele Elemente enthalten soll
    gruppe_sizes[:len(X) % k] += 1 # Falls die Länge des Datensatzes nicht restlos durch k teilbar ist, wird der Rest auf die ersten Gruppen verteilt

    gruppen = []
    aktuell = 0
    # Index-Paare zum Splitten der Daten in Test- und Trainingsdaten
    for gruppe_size in gruppe_sizes:
        start, stop = aktuell, aktuell + gruppe_size
        test_idx = indices[start:stop] # Testdaten setzten -> aktuelle Gruppe
        train_idx = np.concatenate((indices[:start], indices[stop:])) # Trainingsdaten setzen -> alles andere außerhalb der aktuellen Gruppe
        gruppen.append((train_idx, test_idx))
        aktuell = stop
    return gruppen

# Hilfsfunktion: MQF
def mittel_quad_fehler(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# Hauptfunktion mit Rückgabe
def polynome_kreuzvalidieren(X, y, k, plot_models=True):
    bester_grad = None # merkt sich den aktuell besten Grad
    lowest_total_mqf = float('inf')  # merkt sich den kleinsten MQF und beginnt bei unendlich
    mqf_werte = {} # Dictionary für MQF pro Polynomgrad

    x_plot = np.linspace(X.min(), X.max(), 500).reshape(-1, 1)  # Für Plot: erzeugt 500 gleichmäßig verteilte Werte innerhalb von min und max von X als 2-dim. Array

    # falls eine grafische Darstellung gewünscht ist
    if plot_models:
        plt.figure(figsize=(10, 6)) # neune Plott erstellen
        plt.scatter(X, y, label="Daten", color='black', alpha=0.6) # Streudiagramm der Originaldaten zeichnen

    # Schleife über alle Polynomgrade 1-4
    for grad in range(1, 5):
        total_mqf = 0
        X_poly = polynomial_features(X, grad) # erzeugt Polynomfeatures für X bis zum angegebenen Grad
        folds = teile_in_k_gruppen(X_poly, k) # Zerteilt die Daten in k Gruppen

        for train_idx, test_idx in folds: # Schleife über alle Gruppen
            # zerteilen der Polynomdaten und Zielwerte in Trainingsdaten und Testdaten
            X_train, X_test = X_poly[train_idx], X_poly[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]

            # lineares Regressionsmodell erzeugen und mit Trainingsdaten trainieren
            model = LinearRegression()
            model.fit(X_train, y_train)
            # Vorhersagen auf den Testdaten machen
            y_pred = model.predict(X_test)

            # MQF berechnen und zur MQF summe für den aktuellen Grad zählen
            mqf = mittel_quad_fehler(y_test, y_pred)
            total_mqf += mqf

        # MQS Summe für den aktuellen Grad im Dictrionary speichern
        mqf_werte[grad] = total_mqf
        print(f"Grad {grad}: Summe MQF über {k} Gruppen = {total_mqf:.4f}")
        durchschnitt_mqf = total_mqf / k
        print(f"Grad {grad}: Durchschnittlicher MQF = {durchschnitt_mqf:.4f}")

        # wenn dieser Grad einen kleineren Fehler als der bisher beste hat, dann als neuen besten Grad speichern und kleinsten MQF aktualisieren
        if total_mqf < lowest_total_mqf:
            lowest_total_mqf = total_mqf
            bester_grad = grad

        # wenn ein Plott gewünscht ist, dann Modell auf alle Daten trainieren, Vorhersage erzeugen und Modellkurve für den aktuellen Grad zeichnen
        if plot_models:
            model.fit(X_poly, y)
            x_plot_poly = polynomial_features(x_plot, grad)
            y_plot = model.predict(x_plot_poly)
            plt.plot(x_plot, y_plot, label=f'Grad {grad}')

    # Am Ende Plot anzeigen mit Titel, Achsenbeschriftung, Legende und Gitter
    if plot_models:
        plt.title(f"Polynomregression (k={k}-Gruppe KV)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)
        plt.show()

    print(f"\nBestes Modell: Polynom Grad {bester_grad} mit MQF-Summe {lowest_total_mqf:.4f}")
    return bester_grad, mqf_werte

# Beispiel-Daten erzeugen
np.random.seed(0) # Zufallsgenerator mit Startwert um es reproduzierbar zu machen -> war nötig zum debuggen
X = np.sort(5 * np.random.rand(100, 1), axis=0) # 100 Zufallszahlen zwischen 0 und 5 erzeugen, aufsteigend sortiert nach x-Wert
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0]) # Zielwert (sin(Werte aus X)) in einem eindimensionalen Array + Rauschen -> Stichproben aus Gaußverteilung

# Ausführen mit k-Folds
k = 5
bester_grad, mqf_werte = polynome_kreuzvalidieren(X, y, k, plot_models=True)

print("\nAlle MQF-Summen:")
for grad, mqf in mqf_werte.items(): # Schleife über das Dictionary um für jeden Grad die MQF Summe formatiert auszugeben
    print(f"Grad {grad}: {mqf:.4f}")