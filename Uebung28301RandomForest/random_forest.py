import pandas
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

# Einlesen der Daten
df = pandas.read_csv("UniData.csv")

# Vorbereitung der Daten

d = {"Oxford":0, "Harvard":1, "ETH":2}
df["Uni"] = df["Uni"].map(d)

d= {"YES":1, "NO":0}
df["Hire"] = df["Hire"].map(d)

# Trennung der Feature Spalten von der Target-Spalte
features = ["Age", "Experience", "Rank", "Uni"]

X = df[features]
y = df["Hire"]

# Decision Tree Klassifizierer

dtree = DecisionTreeClassifier()
dtree.fit(X,y)

tree.plot_tree(dtree, feature_names=features)

new_data = pandas.DataFrame([[40,10,7,1]], columns=features)

print(dtree.predict(new_data))

rforest = RandomForestClassifier(n_jobs=10)
rforest.fit(X,y)
print(rforest.predict(new_data))
