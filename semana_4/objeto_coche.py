class Coche:

  #Atributos:
  marca = "Ford"
  color = "Rojo"
  ano_fabricacion = "2014"
  claxon = True
  camara_reversa = False

  #Métodos:
  def encender (self):
    print("Encender")

  def apagar (self):
    print("Apagar")

  def __init__ (self):
    pass
    print("Constructor Coche")

class Ford(Coche):

  #Atributos:
  motor_tamano = "2.2 lts."
  tipo_combustible = "Gasolina"
  autonomia = "15 km/l combinado"
  velocidad_max = "220 km/h"
  traccion = "Delantera"

  #Métodos: 
  def acelerar (self):
    print("Acelerar")
  
  def frenar (self):
    print("Frenar")

  def encender (self):
    print("Encender con los cables pelados (chispazo)")

  def apagar (self):
    print("Apagar con la llave.")

  def __init__ (self):
    pass
    print("Constructor FORD:")

fiesta= Ford()
print(fiesta.marca)
print(fiesta.color)
print(fiesta.ano_fabricacion)
print(fiesta.claxon)
print(fiesta.camara_reversa)
print(fiesta.motor_tamano)
print(fiesta.tipo_combustible)
print(fiesta.autonomia)
print(fiesta.velocidad_max)
print(fiesta.traccion)
fiesta.encender()
fiesta.apagar()
fiesta.acelerar()
fiesta.frenar()
