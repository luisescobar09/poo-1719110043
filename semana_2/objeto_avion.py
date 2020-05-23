class Avion:

  #Atributos:
  color = "blanco."
  valocidad_max = "1040 k/h."
  tipo_combustible = "JET A1"
  luces= True
  ventanas = True
  puertas = True
  numero_pasillos = "2 pasillos"
  motor = True
  aire_acondicionado = True
  bolsas_aire = True

  #Métodos:
  def volar (self):
    print("Volar")

  def encender (self):
    print("Encender")
  
  def apagar (self):
    print("Apagar")
  
  def despegar (self):
    print("Despegar")
  
  def acelerar (self):
    print("Acelerar")

  def __init__ (self):
    print("Constructor Avion")

objeto_avion = Avion()

print("Atributos:")
print(objeto_avion.color)
print(objeto_avion.valocidad_max)
print(objeto_avion.tipo_combustible)
print(objeto_avion.luces)
print(objeto_avion.ventanas)
print(objeto_avion.puertas)
print(objeto_avion.numero_pasillos)
print(objeto_avion.motor)
print(objeto_avion.aire_acondicionado)
print(objeto_avion.bolsas_aire)

print("Métodos:")
objeto_avion.volar()
objeto_avion.encender()
objeto_avion.apagar()
objeto_avion.despegar()
objeto_avion.acelerar()