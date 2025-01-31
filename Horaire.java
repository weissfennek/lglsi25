public class Horaire {
    private int h,m,s;
    public Horaire(int h){
        this.h=h;
        this.m=0;
        this.s=0;
    }
    public Horaire(int h,int m,int s){
        this.h=h;
        this.m=m;
        this.s=s;
    }
    public Horaire(int h,int m){
        this.h=h;
        this.m=m;
        this.s=0;
    }
    public void afficher(){
        System.out.println("il est :"+h+" ,minite :"+m+" seconde :"+s);

    }
    public int Difference(Horaire k){
        int sec=this.h*3600+this.m*60+this.s;
        int sech=k.h*3600+k.m*60+k.s;
        int def;
        def=Math.abs(sec-sech);
        return def;


    }
    public int geth() {
        return h;
    }

    public void seth(int h) {
        this.h = h;
    }

    public int getm() {
        return m;
    }

    public void setm(int m) {
        this.m = m;
    }

    public int gets() {
        return s;
    }

    public void sets(int s) {
        this.s = s;
    }

}
