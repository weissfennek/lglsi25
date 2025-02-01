def compter_voyelles(phrase):
    voyelles = "aeiouAEIOU"
    compteur = sum(1 for c in phrase if c in voyelles)
    return compteur
