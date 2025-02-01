package inverse;
import java.util.Scanner;
public class InverseMotsMain {
	 public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);

	        System.out.print("Entrez une phrase : ");
	        String phrase = scanner.nextLine();

	        String phraseInversee = InverseMotsUtils.inverserMots(phrase);

	        System.out.println("Phrase avec mots inversés : " + phraseInversee);

	        scanner.close();
	    }

}
