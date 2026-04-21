import pandas as pd
from sklearn import linear_model

fish = pd.read_csv("K4.0026_2.3.2.Ü.01_Fish.csv")
print(fish.to_string())
ohe_species = pd.get_dummies(fish[["Species"]])
print(ohe_species.to_string())
X = pd.concat([fish[["Weight", "Length", "Height"]],ohe_species], axis=1)
y = fish["Width"]

regr = linear_model.LinearRegression()
regr.fit(X, y)
predicted_width = regr.predict([[233, 20.3, 13.32, 0,0,0,0,0,0,1]])
print(predicted_width)