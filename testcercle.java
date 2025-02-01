public class textcercle {

	public static void main(String[] args) {
		Cercle c1 = new Cercle(3.2,"Rouge");
		Cercle c2= new Cercle(5.0,"Noire");
		System.out.println("la surface de cercle c1 est : "+c1.getSurface());
		System.out.println("la surface de cercle c2 est : "+c2.getSurface());
		System.out.println("le perimetre de cercle c1 est : "+c1.getPerimetre());
		System.out.println("le perimetre de cercle c2 est : "+c2.getPerimetre());
		c1.setCouleur("bleu");
		System.out.println("la couleur de cercle c1 est " +c1.getCouleur());
		
		
	}

}