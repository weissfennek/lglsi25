def est_bissextile(annee):
    """
    Vérifie si une année est bissextile.
    Une année est bissextile si :
    - Elle est divisible par 4 et non par 100, ou
    - Elle est divisible par 400.
    """
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Saisie de l'année par l'utilisateur
if __name__ == "__main__":
    try:
        annee = int(input("Entrez une année : "))
        if est_bissextile(annee):
            print(f"L'année {annee} est bissextile.")
        else:
            print(f"L'année {annee} n'est pas bissextile.")
    except ValueError:
        print("Veuillez entrer une année valide (un nombre entier).")
