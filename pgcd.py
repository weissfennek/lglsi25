#a fonction suivante retourne le pgcd de deux nombre passer en parametres
from math import *
def pgcd(a, b):
    while a != b :
        if a== 0 :
            return b
        if b== 0 :
            return a
        if abs(a) > abs(b):
            a =abs(a)- abs(b)
        else:
            b = abs(b)- abs(a)
    return a