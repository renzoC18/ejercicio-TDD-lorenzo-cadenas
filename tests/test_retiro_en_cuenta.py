import unittest
from src.cuenta import Cuenta
class TestIngresoEnCuenta(unittest.TestCase):
    def test_cuando_retiras_cuenta_nueva_excepcion_falta_saldo(self) -> None:
        cuenta = Cuenta()

        with self.assertRaises(ValueError):
            cuenta.retirar(500)

        self.assertEqual(cuenta.saldo,0)#Ahora vemos que tenemos que definir la variable saldo en Cuenta

    def test_cuando_retiras_cuenta_existente_menor_saldo(self) -> None:
        cuenta = Cuenta()
        cuenta.ingresar(500)
    
        with self.assertRaises(ValueError):
            cuenta.retirar(600)

        self.assertEqual(cuenta.saldo,500)

    def test_cuando_retiras_cuenta_existente_mayor_saldo(self) -> None:
        cuenta = Cuenta()
        cuenta.ingresar(1000)
        cuenta.retirar(600)

        self.assertEqual(cuenta.saldo,400)

    
if __name__== '__main__':
    unittest.main()