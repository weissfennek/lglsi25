def calculer_imc(poids, taille):
    return poids / (taille ** 2)
def test_calculer_imc():

    poids1 = 70  # kg
    taille1 = 1.75  # m
    imc1 = calculer_imc(poids1, taille1)
    assert round(imc1, 2) == 22.86, f"Erreur: IMC attendu 22.86, obtenu {imc1}"
    print("Cas de test 1 réussi")

    poids2 = 50  # kg
    taille2 = 1.60  # m
    imc2 = calculer_imc(poids2, taille2)
    assert round(imc2, 2) == 19.53, f"Erreur: IMC attendu 19.53, obtenu {imc2}"
    print("Cas de test 2 réussi")

    poids3 = 85  # kg
    taille3 = 1.70  # m
    imc3 = calculer_imc(poids3, taille3)
    assert round(imc3, 2) == 29.41, f"Erreur: IMC attendu 29.41, obtenu {imc3}"
    print("Cas de test 3 réussi")

if __name__ == "__main__":
    test_calculer_imc() 



