#Paso 1: Creamos cuenta tras error inicial
class Cuenta:
    #pass
    saldo=0

#Paso 2: Da error porque no existe clase cuenta
#Paso 3: Da error porque no existe atributo saldo
#paso 4: Creamos el método ingresar
    def ingresar(self, cantidad: float) -> None:
        self.saldo += cantidad

#Paso 5: Creamos el método retirar

    def retirar(self, cantidad: float) -> None:
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        else:
            self.saldo -= cantidad



