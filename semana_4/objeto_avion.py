class Avion:

  #Atributos:
  color = "blanco."
  tipo_avion= "Pasajeros"
  luces= True
  ventanas = True
  puertas = True

  #Métodos:
  def encender (self):
    print("Encender")
  
  def apagar (self):
    print("Apagar")

  def __init__ (self):
    pass
    print("Constructor Avion")

class AvionPasajeros(Avion):

  #Atributos:
  valocidad_max = "945 k/h."
  tipo_combustible = "JET A1"
  numero_pasillos = "3 pasillos"
  aire_acondicionado = True
  bolsas_aire = True

  #Métodos: 
  def despegar (self):
    print("Despegar")
  
  def acelerar (self):
    print("Acelerar")

  def encender (self):
    print("Encender al accionar el motor")
  
  def apagar (self):
    print("Apagar al aterrizar")

  def __init__ (self):
    pass
    print("Constructor Avión pasajeros:")

boeing747= AvionPasajeros()
print(boeing747.color)
print(boeing747.tipo_avion)
print(boeing747.luces)
print(boeing747.ventanas)
print(boeing747.puertas)
print(boeing747.valocidad_max)
print(boeing747.tipo_combustible)
print(boeing747.numero_pasillos)
print(boeing747.aire_acondicionado)
print(boeing747.bolsas_aire)
boeing747.encender()
boeing747.apagar()
boeing747.despegar()
boeing747.acelerar()
