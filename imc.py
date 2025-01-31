def calculer_imc(poids, taille):
    return poids / (taille ** 2)
poids = float(input("Entrez votre poids en kilogrammes: "))
taille = float(input("Entrez votre taille en mètres: "))
imc = calculer_imc(poids, taille)
if imc < 18.5:
    categorie = "Insuffisance pondérale"
elif 18.5 <= imc < 24.9:
    categorie = "Poids normal"
elif 25 <= imc < 29.9:
    categorie = "Surpoids"
else:
    categorie = "Obésité"
    
print(f"Votre IMC est de {imc:.2f}. Catégorie: {categorie}")