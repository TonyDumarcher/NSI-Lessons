import math

def paf(somme, n):
    print(n, somme)
    if n <= 0:
        return 3-somme
    somme +=(((-1)**n)*2) / (n*(2*n+1)*(2*n+2))
    return paf(somme, n-1)
    

def pi(somme, n):
    return paf(somme,n)

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
