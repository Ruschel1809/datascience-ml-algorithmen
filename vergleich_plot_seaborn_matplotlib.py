# Ziel: Scatterplot von "Battery Power" gegen "Price", farblich gruppiert nach "Price Range"
#  Beispiel mit matplotlib (klassisch)

import pandas as pd
import matplotlib.pyplot as plt

# CSV laden
df = pd.read_csv('CaseStudy202\\K4.0026_2.C.02_MobilePhone.csv')

# 1️ Kürzel in lesbare Werte umwandeln
price_mapping = {
    'l': 'Low',
    'm': 'Medium',
    'h': 'High'
}
df['Price Range'] = df['Price Range'].map(price_mapping)

# 2️ Farben für die Preiskategorien
colors = {'Low': 'green', 'Medium': 'orange', 'High': 'red'}

# 3️ Scatterplot
plt.figure(figsize=(8, 6))
for label in df['Price Range'].unique():
    subset = df[df['Price Range'] == label]
    plt.scatter(subset['battery_power'], subset['Price Range'],
                c=colors[label], label=label, alpha=0.6)

plt.xlabel('Battery Power')
plt.ylabel('Price')
plt.title('Battery Power vs Price by Price Range')
plt.legend()
plt.grid(True)
plt.show()
#  Was passiert hier?
#
# Du musst selbst filtern nach den Gruppen (df[df['Price Range'] == label])
#
# Du weist manuell Farben zu
#
# Du baust Legende und Achsentitel selbst



# # Beispiel mit seaborn (einfach & elegant)
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=df, x='Battery Power', y='Price', hue='Price Range', palette='Set2')
# plt.title('Battery Power vs Price by Price Range')
# plt.grid(True)
# plt.show()
#
# #  Was ist anders?
# #
# # Kein manuelles Filtern – seaborn erkennt automatisch die Gruppen
# #
# # Farben und Legende werden automatisch gesetzt
# #
# # Viel weniger Code, gleiche (bessere) Wirkung
#
# #  Vergleich
# # Feature | matplotlib | seaborn
# # Syntax | Ausführlicher | Kürzer & automatisiert
# # Farbschema | Manuell | Automatisch (aber anpassbar)
# # Gruppierung nach Farben | Manuell | Automatisch mit hue
# # Stil | Klassisch, einfacher	| Moderner, oft ansprechender