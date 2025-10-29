import unittest
from src.cuenta import Cuenta
class TestIngresoEnCuenta(unittest.TestCase):
    def test_cuando_ingreso_cuenta_nueva_saldo_aumenta_ingreso_inicial(self) -> None:
        cuenta = Cuenta()
        cuenta.ingresar(500)

        self.assertEqual(cuenta.saldo,500)#Ahora vemos que tenemos que definir la variable saldo en Cuenta

    def test_cuando_ingreso_cuenta_existente_saldo_aumenta(self) -> None:
        cuenta = Cuenta()
        cuenta.ingresar(500)
        cuenta.ingresar(1500)
        self.assertEqual(cuenta.saldo,2000)

    
if __name__== '__main__':
    unittest.main()