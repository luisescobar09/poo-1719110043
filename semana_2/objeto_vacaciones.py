class Vacaciones:

  #Atributos:
  nombre_vacaciones = "Vacaciones de fin de año"
  dia_festivo = "25 de diciembre"
  lugar_turistico = "playa"
  espacio_turistico= "museo"
  espacio_deportivo = "Unidad deportiva"
  cine = "Cimemex"
  videojuego = "FIFA 20"
  viajes = True
  periodo_vacacional = "22 de diciembre a 08 enero"
  comida = "Pavo"

  #Métodos:
  def jugar (self):
    print("Jugar")

  def pasear (self):
    print("Pasear")
  
  def descansar (self):
    print("Descansarr")
  
  def dormir (self):
    print("DOrmir")
  
  def convivir (self):
    print("Convivir")

  def __init__ (self):
    print("Constructor Vacaciones")

objeto_vacaciones = Vacaciones()

print("Atributos:")
print(objeto_vacaciones.nombre_vacaciones)
print(objeto_vacaciones.dia_festivo)
print(objeto_vacaciones.lugar_turistico)
print(objeto_vacaciones.espacio_turistico)
print(objeto_vacaciones.espacio_deportivo)
print(objeto_vacaciones.cine)
print(objeto_vacaciones.videojuego)
print(objeto_vacaciones.viajes)
print(objeto_vacaciones.periodo_vacacional)
print(objeto_vacaciones.comida)

print("Métodos:")
objeto_vacaciones.jugar()
objeto_vacaciones.pasear()
objeto_vacaciones.descansar()
objeto_vacaciones.dormir()
objeto_vacaciones.convivir()