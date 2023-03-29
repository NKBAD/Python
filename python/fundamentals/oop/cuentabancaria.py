class CuentaBancaria:
        nombre_banco = "BancoDojo"
        todas_las_cuentas =[]

        def __init__(self , tasa_intereses , balance):
            self.tasa_intereses = tasa_intereses
            self.balance = balance


        def deposito(self , amount):
            self.balance+=amount
            return self
        
        def retiro (self , amount):
            self.balance -=amount
            return self
        
        def mostrar_info_cuenta (self ):
            print(f" el monto del balance es igual a   {self.balance}  el monto de interes {self.tasa_intereses}")
            return self
        
        def generar_interés(self):
            # tu código aquí
            self.balance += self.balance * self.tasa_intereses
            return self
        
cuenta1 = CuentaBancaria(0.5,10000)

cuenta1.deposito(500).deposito(400).deposito(50).generar_interés().mostrar_info_cuenta() 

print((10000 + 950))
print((10000 + 950) * 0.5)
print((10000 + 950) + (10000 + 950) * 0.5)