ublic class Crayon {
	private  double epaisseur;
	private double longeur ;
	public Crayon(double epaisseur ,double longeur )
	{
		this.epaisseur=epaisseur;
		this.longeur=longeur;
		
		}
	public double getepaisseur( )
	{
		return epaisseur;
		
		
	}
	public void changeepaisseur(double epaisseur )
	{
		if(epaisseur>0)
			this.epaisseur=epaisseur;
	}

	public double getlongeur( )
	{
		return longeur;
		
		
	}
	public void changelongeur(double longeur )
	{
		if(longeur>0)
			this.longeur=longeur;
	}
	public void description()
	{
		System.out.println("longeur"+longeur+"epaiseur"+epaisseur);
	}


}
