pi = 3.14159

# fonction qui renvoie l'aire d'un disque
def disque(rayon, dec = -1):
    aire = pi * rayon**2
    if dec >= 0:
        aire = round(aire, dec)
    return aire

# fonction qui renvoie l'aire d'un rectangle
def rectangle(largeur, longueur):
    return largeur * longueur

# fonction qui renvoie l'aire d'un triangle
def triangle(base, hauteur):
    return base * hauteur / 2

def main():
    print("Calcul d'aires")
    print("Disque : pi * r^2")
    print("Exemple avec r = 5")
    print("Aire = ", disque(5))
    
if __name__ == "__main__":
    main()