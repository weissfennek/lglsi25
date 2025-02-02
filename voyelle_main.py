import voyelle_utils 

def main():
    phrase = input("Entrez une phrase : ")
    nombre_voyelles = voyelle_utils.compter_voyelles(phrase)
    print("Nombre de voyelles dans la phrase :", nombre_voyelles)

if __name__ == "__main__":
    main()
