public class Cercle {
	

		private double rayon ;
		private String couleur ;
		public double getRayon() {
			return rayon;
		}
	Cercle(double rayon , String couleur){
		this.rayon = rayon ;
		this.couleur=couleur;
		
		
	}
	public void setRayon(double rayon) {
		this.rayon = rayon ;
	}
	public String getCouleur() {
		return couleur;
	}
	public void setCouleur(String couleur) {
		this.couleur = couleur;
	}
	public double getSurface() {
		return (Math.pow(rayon, 2)*Math.PI);
	}
	public double getPerimetre() {
		return(Math.PI*rayon*2);
	}}