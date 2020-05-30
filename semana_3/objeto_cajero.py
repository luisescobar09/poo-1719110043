class CajeroAutomatico:

  #Atributos:
  tipo_cajero = "Full"
  sistema_operativo = True
  seguridad = True
  teclas = True
  hora = True

  #Métodos:
  def encender (self):
    print("Encender")

  def apagar (self):
    print("Apagar")

  def __init__ (self):
    pass
    print("Constructor Cajero Automatico")

class Full(CajeroAutomatico):

  #Atributos:
  pantalla_tactil = True
  fecha = True
  dimensiones = "5x1x2 m."
  tamano = "Grande"
  peso = "19 kilos"

  #Métodos: 
  def retirar (self):
    print("Retirar")
  
  def depositar (self):
    print("Depositar")
  
  def __init__ (self):
    pass
    print("Constructor Full:")

fullBancos= Full()
print(fullBancos.tipo_cajero)
print(fullBancos.sistema_operativo)
print(fullBancos.seguridad)
print(fullBancos.teclas)
print(fullBancos.hora)
print(fullBancos.pantalla_tactil)
print(fullBancos.fecha)
print(fullBancos.dimensiones)
print(fullBancos.tamano)
print(fullBancos.peso)
fullBancos.encender()
fullBancos.apagar()
fullBancos.retirar()
fullBancos.depositar()
