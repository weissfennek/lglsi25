import unittest
from Bissextile import est_bissextile  # Assurez-vous que le fichier s'appelle bien Bissextile.py

class TestBissextile(unittest.TestCase):

    def test_annee_bissextile_divisible_par_4_non_par_100(self):
        self.assertTrue(est_bissextile(2024))  # 2024 est bissextile
        self.assertTrue(est_bissextile(2004))  # 2004 est bissextile

    def test_annee_non_bissextile_divisible_par_100_non_par_400(self):
        self.assertFalse(est_bissextile(1900))  # 1900 n'est pas bissextile
        self.assertFalse(est_bissextile(2100))  # 2100 n'est pas bissextile

    def test_annee_bissextile_divisible_par_400(self):
        self.assertTrue(est_bissextile(2000))  # 2000 est bissextile
        self.assertTrue(est_bissextile(1600))  # 1600 est bissextile

    def test_annee_non_bissextile(self):
        self.assertFalse(est_bissextile(2023))  # 2023 n'est pas bissextile
        self.assertFalse(est_bissextile(1999))  # 1999 n'est pas bissextile

    def test_annee_negative(self):
        self.assertTrue(est_bissextile(-4))    # -4 est bissextile
        self.assertFalse(est_bissextile(-100)) # -100 n'est pas bissextile

if __name__ == "__main__":
    unittest.main()
