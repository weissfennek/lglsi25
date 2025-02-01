
import java.util.Scanner;


public class robot {
	

	
	
		private int x ;
	private int y ;
	private int orientation ;
	robot (int x , int y, int orientation){
		this.x= x;
		this.y= y;
		this.orientation=orientation;
		
	}
	public void deplacer () {
		
		switch (orientation) {
			case 1:
				y=y+1;
				break ;
			case 2:
				x=x+1;
				break ;
			case 3:
				y=y-1;
				break ;
			case 4:
				x=x-1;
				break ;}
				
				
			
		
		
		
		
		
		
	}

	public void tourner () {
		switch (orientation) {
		case 1:
			orientation=2;
			break ;
		case 2:
			orientation=3;
			break ;
		case 3:
			orientation=4;
			break ;
		case 4:
			orientation=1;
			break ;}
		
		
	}
	public void afficher() {

	System.out.println("la position de robot est x:"+x+"y:"+y);
		switch (orientation) {
			case 1:
				System.out.println("le robot rst orientee a nord");
				break ;
			case 2:
				System.out.println("le robot est orientee au est");
				break ;
			case 3:
				System.out.println("le robot est orientee a sud");
				break ;
			case 4:
				System.out.println("le robot est orientee a ouest");
				break ;}
			
			
	}} {
    
}
