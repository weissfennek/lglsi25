public class TestPoint {
	public static void main(String[]args) {
		Point p1=new Point (2.5,3.4);
		Point p=new Point (1.5,2.3);
		System.out.println(p1.position());
		System.out.println(p1.move(2.1, 3.1));
		System.out.println("la distance est"+p1.distance(p));
	}
	
