abstract class Cheval {
    private final int id ;
    private  String nom;
     private int age ;
     Cheval (int id , String nom , int age ){
         this.id = id ; this.nom=nom;this.age = age; }
     abstract double  performance ();
     protected  int getId(){
         return id ;
        
     }
     
     protected String getNom(){
         return nom;
     }
     protected  int getAge(){
          return age ;
     
         
         
     }
     
     public void afficherDetails(){
         System.out.println(" id    : "+id + " nom  :"+ nom + "age   : " + age );
     }
     @Override
    public String toString() {
        return "ID: " + getId() + ", Nom: " + getNom() + ", Âge: " + getAge() + " ans";
    }
    
    } interface competitf{
         public  void participerCourse();
          public void gagnerCourse() ;
    }
     class ChevalCourse extends Cheval implements competitf{
         private double vitesseMax ;
         ChevalCourse( int id , String nom , int age ,double vitesseMax){
             super ( id , nom ,age );
             this.vitesseMax = vitesseMax ;
         }
         public void participerCourse() {
              System.out.println( "ce cheval est participer au course ");
             
         }
         public void gagnerCourse() {
              System.out.println( " ce cheval a gagne la corse ") ;
         }
         public double  performance(){
             return vitesseMax * 2 ;
             
         }
         
         
     }
    class Poney extends Cheval{
        private final  int taille ;
        Poney (int id , String nom , int age, int taille ) {
            super ( id , nom ,age );
        this.taille= taille;}
        public double performance() {
            return (taille * super.getAge() );
        }
     }
     class Eucurie{
         public static String  nomEucurie ;
         Cheval [] tabCheveaux = new Cheval[20];
         static int nb ;
         public void ajouterCheval (Cheval che){
             if ( nb < tabCheveaux.length){
                 tabCheveaux[nb]= che;
                 nb++;
             }  System.out.println( " ce cheval est ajoute succesivemtnt au tableau ");
             
         }
         public void afficherCheveaux () {
             System.out.println("la liste des chevaux sont ") ;
             for ( Cheval ch : tabCheveaux){
                 if ( ch!=null){
                 System.out.println(ch );
                 
             }}
              
     }}
    
    
    
    
    
    
        
    public class GestionDesCheveaux{
        public static void main ( String [] args ){
            Eucurie e1 = new Eucurie ();
            e1.ajouterCheval( new ChevalCourse( 789 ,"jolie ",10 , 100));
            e1.ajouterCheval( new Poney ( 777 , "beau " , 5 , 170));
            e1.ajouterCheval( new Poney ( 888, "bello " , 8 , 200));
            e1.afficherCheveaux();
            (ChevalCourse)e1.gagnerCourse();
            (ChevalCourse)e1.participerCourse();
            for ( Cheval ch : tabCheveaux){
                 if ( ch!=null && ch instanceof ){
                    
            
            
        }
    }	 
     