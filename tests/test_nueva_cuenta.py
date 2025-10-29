import unittest
from src.cuenta import Cuenta
class TestNuevaCuenta(unittest.TestCase):
    def test_nueva_cuenta(self) -> None:
        cuenta = Cuenta()
        self.assertEqual(cuenta.saldo,0)
    
if __name__== '__main__':
    unittest.main()