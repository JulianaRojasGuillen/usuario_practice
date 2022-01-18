from Usuario import Usuario

gaby = Usuario("Gaby")
martha = Usuario ("Martha")
cilo = Usuario ("Cilo")

gaby.balance_cuenta=0
martha.balance_cuenta=0
cilo.balance_cuenta=0

gaby.hacer_deposito(100)
gaby.hacer_deposito(20)
gaby.hacer_deposito(30)
gaby.hacer_retiro(5)
gaby.mostrar_balance_usuario()

martha.hacer_deposito(1000)
martha.hacer_retiro(50)
martha.hacer_retiro(40)
martha.mostrar_balance_usuario()

cilo.hacer_deposito(2000)
cilo.hacer_retiro(500)
cilo.hacer_retiro(300)
cilo.mostrar_balance_usuario()

gaby.mostrar_balance_usuario()
cilo.mostrar_balance_usuario()
martha.mostrar_balance_usuario()

gaby.transfer_dinero(cilo, 5)
martha.transfer_dinero(gaby, 15)
gaby.mostrar_balance_usuario()
martha.mostrar_balance_usuario()
cilo.mostrar_balance_usuario()
