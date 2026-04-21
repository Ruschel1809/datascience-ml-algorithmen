def insertion_sort(liste):
    for i in range(1, len(liste)):
        key = liste[i]
        j = i - 1
        # Verschiebe größere Elemente nach rechts
        while j >= 0 and liste[j] > key:
            liste[j + 1] = liste[j]
            j -= 1
        # Füge das Element an der richtigen Stelle ein
        liste[j + 1] = key
    return liste

liste = [8,2,6,4,5]
print(insertion_sort(liste))

#
# 1. Standard In-Place Insertion Sort (wie oben gezeigt)
# def insertion_sort(liste):
#     for i in range(1, len(liste)):
#         key = liste[i]
#         j = i - 1
#         while j >= 0 and liste[j] > key:
#             liste[j + 1] = liste[j]
#             j -= 1
#         liste[j + 1] = key
#     return liste
#
# Eigenschaften:
#
# In-place (kein zusätzlicher Speicher)
#
# Stabil (gleiche Elemente behalten ihre Reihenfolge)
#
# Einfach & effizient für kleine Listen
#


# 2. Funktionale Version (nicht in-place, gibt eine neue Liste zurück)
# def insertion_sort_functional(liste):
#     sorted_list = []
#     for item in liste:
#         inserted = False
#         for i in range(len(sorted_list)):
#             if item < sorted_list[i]:
#                 sorted_list.insert(i, item)
#                 inserted = True
#                 break
#         if not inserted:
#             sorted_list.append(item)
#     return sorted_list
#
# Eigenschaften:
#
# Gibt eine neue Liste zurück (verändert das Original nicht)
#
# Auch stabil
#
# Klar verständlich
#
# Nicht so effizient für große Listen, weil insert() teuer ist (O(n))
#


# 3. Optimierte Insertion Sort mit Binärer Suche
#
# Die Idee: Suche die richtige Position mit einer binären Suche (O(log n)) statt linear durchzugehen.
#
# Benötigt: Eine Hilfsfunktion
# import bisect
#
# def insertion_sort_binary(liste):
#     sorted_list = []
#     for item in liste:
#         # Finde die richtige Position (binäre Suche)
#         index = bisect.bisect_left(sorted_list, item)
#         sorted_list.insert(index, item)
#     return sorted_list
#
# Eigenschaften:
#
# Nutzt das bisect-Modul für binäre Suche
#
# Effizienter als die lineare Einfügesuche bei vielen Elementen
#
# Nicht in-place
#


# 4. In-Place Insertion Sort mit Binärer Suche (fortgeschritten)
#
# def binary_search(arr, key, start, end):
#     while start < end:
#         mid = (start + end) // 2
#         if arr[mid] < key:
#             start = mid + 1
#         else:
#             end = mid
#     return start
#
# def insertion_sort_binary_inplace(liste):
#     for i in range(1, len(liste)):
#         key = liste[i]
#         pos = binary_search(liste, key, 0, i)
#         # Verschiebe Elemente nach rechts
#         for j in range(i, pos, -1):
#             liste[j] = liste[j - 1]
#         liste[pos] = key
#     return liste