# import time as t
# liste=[[1,2,3],[6,5,3,3],[54,3]]
# time1=t.time()
# print(time1)
# for l in liste:
#     print(sum(l))
# print(t.time()-time1)


# Musterlösung
# Wir haben hier eine Liste mit drei Elementen, jedes Element wiederum ist eine eigene Liste.
# Um von jeder dieser Teillisten die Summe der Elemente zu bekommen, müssen wir in der ersten
# for-Schleife durch alle Listen in der Hauptliste durchgehen und dann für jede Teilliste eine
# eigene for-Schleife aufmachen, um die Elemente zu addieren. Dadurch entsteht eine verschachtelte
# for-Schleife. Wenn wir jetzt die Anzahl der Eingabeelemente verdoppeln – wir haben also doppelt
# so viele Teillisten – dann vervierfacht sich die Anzahl der Durchgänge, die die Schleifen durchlaufen
# müssen. Ein weiterer Algorithmus, der zum Sortieren von Listen verwendet wird, ist der sogenannte
# Insertion Sort, der ebenfalls eine quadratische Komplexität hat. Diesen werden wir jetzt bei einer
# Übung kennenlernen.

# time2=t.time()
# print(time2)
# for l in liste:
#     sum = 0
#     for l2 in l:
#         sum += l2
#     print(sum)
# print(t.time()-time2)

# für genauere Messung timeit
import timeit

liste = [[1,2,3],[6,5,3,3],[54,3]]
# Erzeuge eine Liste mit 1000 Unterlisten à 1000 Elemente
liste2 = [list(range(100)) for _ in range(100)]

# Built-in sum()
def use_sum():
    for l in liste2:
        sum(l)

# Manuelle Schleife
def manual_sum():
    for l in liste2:
        total = 0
        for x in l:
            total += x

print("Built-in sum:", timeit.timeit(use_sum, number=100000))
print("Manual sum:  ", timeit.timeit(manual_sum, number=100000))

#Mit dem dis-Modul kannst du Python-Bytecode analysieren und sehen, was intern passiert:
#import dis

# def concat_slow():
#     result = []
#     for l in liste:
#         result += l
#
# print(dis.dis(concat_slow))
#result += l hängt nicht einfach nur eine Referenz an – da passiert mehr, und das erklärt die Performance-Unterschiede