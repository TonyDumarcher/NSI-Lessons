import math

def paf(somme, n, fin):
    print(n)
    if n >= fin:
        return somme
    somme +=(((-1)**n)*2) / (n*(2*n+1)*(2*n+2))
    return paf(somme, n+1, fin)
    

def pi(somme, n):
    nb_rec = n // 997 
    last = n % 997
    somme = 0
    debut = 1
    for rec in range(nb_rec):
        somme = paf(somme, debut, debut + 997)
        debut += 997
    somme = paf(somme, debut, debut + last)
    return 3-somme

n_input = None
while True:
    
    n_input = input("Entrez un nombre ou q pour quitter:")
    if n_input.isdigit():
        n_input = int(n_input)
        n_pi = pi(0, n_input)
    elif n_input == "q":
        break
    else:
        print("Input invalide, réessayez")
        continue
    print("")
    print("===================")
    print("")
    print("Notre pi :")
    print(n_pi)
    print("")
    print("Le vrai pi:")
    print(math.pi)
    print("")
    
    print("Différence:")
    print(n_pi - math.pi)
