public class test_Horaire {
    public static void main(String[] args) {
        

        Horaire h1 =new Horaire(14);
        Horaire h2=new Horaire(15,12);
        Horaire h3=new Horaire(16,17,9);
        h1.afficher();
        h2.afficher();
        h3.afficher();
        int difference=h1.Difference(h3);
        System.out.println("differance entre horaire 1 et 3 :"+difference+" seconde");
        difference=h2.Difference(h3);
        System.out.println("differance entre horaire 2 et 3 :"+difference+" seconde");


    }
    

}
