import numpy as np


def lienare_regression_population(listei: list[int], listej: list[int], x: int):
    mittelwerti = np.mean(listei)
    mittelwertj = np.mean(listej)
    standardabweichungi = np.std(listei)
    standardabweichungj = np.std(listej)
    korrelation = np.corrcoef(listei, listej)[0, 1]
    b = (standardabweichungj/standardabweichungi)*korrelation
    a = -b*mittelwerti + mittelwertj
    print("b: ", b)
    print("a: ", a)
    return b*x+a

listei = [170,180,190]
listej = [42,44,43]
lienare_regression_population(listei, listej, x=160)

