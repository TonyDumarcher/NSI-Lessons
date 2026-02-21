from turtle import *

def rectangle(longueur, largeur, couleur):
    color(couleur)
    for i in range(2):
        forward(longueur)
        right(90)
        forward(largeur)
        right(90)

def triangle(cote, couleur):
    color(couleur)
    for i in range(3):
        forward(cote)
        right(120)

def cercle(rayon, couleur):
    color(couleur)
    circle(rayon)