class Cajero:

  #Atributos:
  interfaz = True
  sistema_operativo = True
  seguridad = True
  teclas = True
  pantalla_tactil = True
  fecha = True
  hora = True
  dimensiones = "5x1x2 m."
  tamano = "Grande"
  peso = "19 kilos"

  #Métodos:
  def encender (self):
    print("Encender")

  def apagar (self):
    print("Apagar")
  
  def pagar (self):
    print("Pagar")
  
  def retirar (self):
    print("Retirar")
  
  def depositar (self):
    print("Depositar")

  def __init__ (self):
    print("Constructor Coche")

objeto_cajero = Cajero()

print("Atributos:")
print(objeto_cajero.interfaz)
print(objeto_cajero.sistema_operativo)
print(objeto_cajero.seguridad)
print(objeto_cajero.teclas)
print(objeto_cajero.pantalla_tactil)
print(objeto_cajero.fecha)
print(objeto_cajero.hora)
print(objeto_cajero.dimensiones)
print(objeto_cajero.tamano)
print(objeto_cajero.peso)

print("Métodos:")
objeto_cajero.encender()
objeto_cajero.apagar()
objeto_cajero.pagar()
objeto_cajero.retirar()
objeto_cajero.depositar()