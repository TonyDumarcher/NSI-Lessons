def somme(liste):
    if liste == []:
        return None
    sommeFinale = 0
    for nombre in liste:
        sommeFinale += nombre
    return sommeFinale

def moyenne(liste):
    if liste == []:
        return None
    return somme(liste) / len(liste)