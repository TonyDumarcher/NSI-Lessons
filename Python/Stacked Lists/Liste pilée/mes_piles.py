def creer_pile(c):
    p = (c + 1) * [None]
    p[0] = 0
    return p

def empiler(p, x):
    if p[0] < len(p) - 1:
        p[0] += 1
        p[p[0]] = x
    return p

def depiler(p):
    if not pile_vide(p):
        val = p[p[0]]
        p[p[0]] = None
        p[0] -= 1
        return val
    return None

def pile_vide(p):
    return p[0] == 0

def taille(p):
    return p[0]

def sommet(p):
    if not pile_vide(p):
        return p[p[0]]
    return None

def vider_pile(p):
    p = creer_pile(len(p)-1)
    return p

def inverse_pile(p):
    pile_inverse = creer_pile(len(p) - 1)
    while not pile_vide(p):
        element = depiler(p)
        empiler(pile_inverse, element)
    return pile_inverse

def inverse_pile_sans_modif(p):
    p_inv = creer_pile(len(p) - 1)
    p_temp = creer_pile(len(p) - 1)
    while not pile_vide(p):
        empiler(p_temp, depiler(p))
    while not pile_vide(p_temp):
        element = depiler(p_temp)
        empiler(p, element)
        empiler(p_inv, element)
    return inverse_pile(p_inv)