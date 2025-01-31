public class Point {
	private double x;
	private double y;
	
public Point() {	
	}
	public Point(double x ,double y) {
		this.x=x;
		this.y=y;
		
	}
	public String position() {
		return ("la position est" + x+","+y);
		
	}
	public String move (double dx,double dy) {
		this.x = this.x + dx ;
		this.y=this.y +dy;
		return ("la nouvelle position est"+ x +","+y);
		
		
	}
	public double distance(Point p) {
		double x=this.x-p.x;
		double y=this.y-p.y;
		double d =x*x+y*y;
		return (Math.sqrt(d));
		
	}
	public double getX() {
		return x;
	}
	public double getY() {
		return y;
	}
public void setX(double x) {
	this.x=x;
}
public void setY(double y) {
	this.y=y;
}

}
