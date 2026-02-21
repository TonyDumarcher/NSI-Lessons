from mes_piles import *

p = creer_pile(3)
print("Pile vide :", p)

empiler(p, 'x')
print("Après empiler 'x' - Taille :", taille(p), "| Sommet :", sommet(p))

v = depiler(p)
print("Élément dépilé :", v, "| Pile vide ?", pile_vide(p))

p = creer_pile(2)
empiler(p, 1)
empiler(p, 2)
p2 = vider_pile(p)
print("\nTest Vider - Pile vide ?", pile_vide(p2))

p = creer_pile(4)
empiler(p, 'A')
empiler(p, 'B')
empiler(p, 'C')
print("\nOriginal avant inversion :", p)
inv = inverse_pile(p)
print("Pile inversée (Q4) :", inv)
print("Sommet de l'inverse :", sommet(inv))

p_original = creer_pile(3)
empiler(p_original, 1); empiler(p_original, 2)
print("\n--- Test Q5 ---")
print("Inverse :", inverse_pile_sans_modif(p_original))
print("Original après (doit être [2, 1, 2, None]) :", p_original)