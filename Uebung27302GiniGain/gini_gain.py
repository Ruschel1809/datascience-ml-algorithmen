from collections import Counter


def gini_index(labels):
    """Berechnet den Gini-Index einer Liste von Labels."""
    total = len(labels)
    if total == 0:
        return 0.0
    label_counts = Counter(labels)
    return 1.0 - sum((count / total) ** 2 for count in label_counts.values())


def split_by_attribute(data, attribute_index):
    """Teilt die Daten basierend auf dem Attributwert (z.B. 'Farbe')."""
    splits = {}
    for row in data:
        key = row[attribute_index]
        label = row[-1]
        if key not in splits:
            splits[key] = []
        splits[key].append(label)
    return splits


def gini_gain(data, attribute_index):
    """Berechnet den Gini-Gain bei Aufteilung nach einem Attribut."""
    labels = [row[-1] for row in data]
    total_gini = gini_index(labels)
    splits = split_by_attribute(data, attribute_index)
    total = len(data)

    weighted_gini = sum(
        (len(subset) / total) * gini_index(subset)
        for subset in splits.values()
    )

    return total_gini - weighted_gini

data = [
    ("Rot", "Apfel"),
    ("Rot", "Apfel"),
    ("Grün", "Apfel"),
    ("Grün", "Birne"),
    ("Gelb", "Banane"),
    ("Gelb", "Banane"),
]


# Musterlösung
# a)	Linker Bereich: 2 blau, 2 rot
#
# Rechter Bereich: 1 blau, 1 rot, 3 grün Gini-Gain: 0.133
#
# b)	Linker Bereich: 3 blau, 3 rot Rechter Bereich: 3 grün Gini-Gain: 0.333
#
# c)	Unterer Bereich: 3 blau, 1 grün Oberer Bereich: 3 rot, 2 grün Gini-Gain: 0.233