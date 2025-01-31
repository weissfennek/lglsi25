from pgcd import pgcd

#test pour un nombre premier
def test_premier():
    assert pgcd(13,15)==1


#test un nombre normal
def test_normal():
    assert pgcd(7,14)==7


#test le zero
def test_zero():
    assert pgcd(0,13)==13


#test un nombre negatif
def test_negatif():
    assert pgcd(-12,4)==4