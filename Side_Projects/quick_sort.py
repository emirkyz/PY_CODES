

def quick_sort(liste: list):
    length = len(liste)
    if length <= 1:
        return liste
    else:
        pivot = liste.pop()

    lower = []
    higher = []

    for items in liste:
        if items < pivot:
            lower.append(items)
        else:
            higher.append(items)

    return quick_sort(lower) + [pivot] + quick_sort(higher)


listem = [5, 21, 2, 1, 51, 72, 45, 36]
sonuc = quick_sort(listem)
print(sonuc)
