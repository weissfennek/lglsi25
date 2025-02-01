package inverse;

public class InverseMotsUtils {   public static String inverserMots(String phrase) {
    String[] mots = phrase.split(" ");
    StringBuilder resultat = new StringBuilder();

    for (String mot : mots) {
        resultat.append(new StringBuilder(mot).reverse()).append(" ");
    }

    return resultat.toString().trim();
}

}
