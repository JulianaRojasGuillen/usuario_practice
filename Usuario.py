class Usuario:
    #constructor
    def __init__(self, nombre):
        self.nombre=nombre
        self.balance_cuenta=0

    #métodos
    def hacer_deposito(self,monto):
        self.balance_cuenta += monto
    
    def hacer_retiro(self,monto):
        self.balance_cuenta -= monto
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: {self.balance_cuenta}")

    def transfer_dinero(self, other_user, monto):
        self.balance_cuenta-=monto
        other_user.balance_cuenta+=monto
        print(f"{self.nombre} transfirió {monto} soles a {other_user.nombre}. Saldo: {self.balance_cuenta} soles")
        
    
