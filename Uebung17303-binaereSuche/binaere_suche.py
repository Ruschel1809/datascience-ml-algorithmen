# !Binäre Suche funktioniert nur auf sortierten Listen!!!!!
def binaere_suche(elem, liste, start=0, end=None):
    if end is None:
        end = len(liste) - 1

    if start > end:
        return None  # nicht gefunden

    pivot = (start + end) // 2

    if liste[pivot] == elem:
        return pivot
    elif elem < liste[pivot]:
        return binaere_suche(elem, liste, start, pivot - 1)
    else:
        return binaere_suche(elem, liste, pivot + 1, end)

def binaere_suche_iterativ(elem, liste):
    start = 0
    end = len(liste) - 1

    while start <= end:
        pivot = (start + end) // 2
        if liste[pivot] == elem:
            return pivot
        elif elem < liste[pivot]:
            end = pivot - 1
        else:
            start = pivot + 1
    return None

liste = [10, 19, 23, 25, 36, 61, 79, 81, 99]
print(binaere_suche_iterativ(7,liste))