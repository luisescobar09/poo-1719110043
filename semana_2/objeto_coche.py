class Coche:

  #Atributos:
  motor_tamano = "2.2"
  numero_cilindros = "4"
  color = "Rojo"
  tipo_combustible = "Diesel"
  autonomia = "13 km/l combinado"
  velocidad_max = "220 km/h"
  traccion = "Delantera"
  ano_fabricacion = "2008"
  claxon = True
  camara_reversa = False

  #Métodos:
  def encender (self):
    print("Encender")

  def apagar (self):
    print("Apagar")
  
  def acelerar (self):
    print("Acelerar")
  
  def frenar (self):
    print("Frenar")
  
  def derrapar (self):
    print("Derrapar")

  def __init__ (self):
    print("Constructor Coche")

objeto_coche = Coche()

print("Atributos:")
print(objeto_coche.motor_tamano)
print(objeto_coche.numero_cilindros)
print(objeto_coche.color)
print(objeto_coche.tipo_combustible)
print(objeto_coche.autonomia)
print(objeto_coche.velocidad_max)
print(objeto_coche.traccion)
print(objeto_coche.ano_fabricacion)
print(objeto_coche.claxon)
print(objeto_coche.camara_reversa)

print("Métodos:")
objeto_coche.encender()
objeto_coche.apagar()
objeto_coche.acelerar()
objeto_coche.frenar()
objeto_coche.derrapar()