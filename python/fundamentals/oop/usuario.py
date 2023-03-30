class Usuario:
    def __init__(self,name,email,balance_cuenta):
        self.name = name
        self.email = email
        self.balance_cuenta = balance_cuenta

    def hacer_deposito(self,amount):
         self.balance_cuenta += amount

    def hacer_giro(self,amount):
        self.balance_cuenta -= amount

guido = Usuario('guido','email@email.cl',0)
nicolás = Usuario("nicolás","email@email",100)

guido.hacer_deposito(150)
nicolás.hacer_deposito(150)
print("el usuario",guido.name,"tiene en su cuenta",guido.balance_cuenta)

guido.hacer_giro(150)
print("el usuario", guido.name,"disminuyó su saldo a",guido.balance_cuenta)
print("el usuario", nicolás.name,"tiene en su cuenta",nicolás.balance_cuenta)