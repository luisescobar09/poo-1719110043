class Vacaciones:

  #Atributos:
  lugar_turistico = "playa"
  espacio_turistico= "museo"
  espacio_deportivo = "Unidad deportiva"
  cine = "Cimemex"
  videojuego = "FIFA 20"

  #Métodos:
  def jugar (self):
    print("Jugar")
  
  def dormir (self):
    print("DOrmir")

  def __init__ (self):
    pass
    print("Constructor Vacaciones")

class NombreVacaciones(Vacaciones):

  #Atributos:
  nombre_vacaciones = "Vacaciones de fin de año"
  dia_festivo = "25 de diciembre"
  viajes = True
  periodo_vacacional = "22 de diciembre a 08 enero"
  comida = "Pavo"

  #Métodos: 
  def descansar (self):
    print("Descansarr")
  
  def convivir (self):
    print("Convivir")

  def __init__ (self):
    pass
    print("Constructor Nombre vacaciones:")

finDeAno= NombreVacaciones()
print(finDeAno.lugar_turistico)
print(finDeAno.espacio_turistico)
print(finDeAno.espacio_deportivo)
print(finDeAno.cine)
print(finDeAno.videojuego)
print(finDeAno.nombre_vacaciones)
print(finDeAno.dia_festivo)
print(finDeAno.viajes)
print(finDeAno.periodo_vacacional)
print(finDeAno.comida)
finDeAno.jugar()
finDeAno.dormir()
finDeAno.descansar()
finDeAno.convivir()
