def BinaryAlgorithm(Llista, left, right, objectiu):
    while (left <= right):
        centre = int(left +(right - left) / 2)
        if ( objectiu == Llista[centre]):
            return ("The number is {}".format(Llista[centre]))
        if (Llista[centre] > objectiu):
                right = centre - 1
        else:
            left = centre + 1 
    return ("Unable to find the selected number")

Llista = [4, 12, 25, 39, 40, 47]
Objectiu = 25
Mida = len(Llista)

resultat = BinaryAlgorithm(Llista, 0, Mida - 1, Objectiu)


print(resultat)
