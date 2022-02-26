from random import shuffle
from math import factorial


def combinations(str):
    allcomb = []  # Aqui armazena todas combinações
    word = [l for l in str]  
    for l in str:
        t = 0  # Quantas combinações uma letra tem
        while t != factorial(len(str)) / len(str):
            word2 = word.copy()
            shuffle(word2)  # Embaralha a lista da palavra
            print(word2)
            if word2 not in allcomb:
                t += 1
                allcomb.append(word2)

    print(allcomb)


combinations('eae')