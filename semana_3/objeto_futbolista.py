class Futbolista:

  #Atributos:
  nacionalidad = "Mexicana"
  equipo = "SC Napoli"
  sexo = "Masculino"
  posicion = "extremo izquierdo o derecho"
  numero_dorsal = "11"

  #Métodos:
  def patearBalon (self):
    print("Patear un balón")

  def pasarBalon (self):
    print("Pasar un balón")

  def __init__ (self):
    pass
    print("Constructor Futbolista")

class EquipoNapoli(Futbolista):

  #Atributos:
  nombre = "Hirving Lozano"
  edad = "24 años"
  estatura = "1.74 metros"
  peso = "72 kg."
  valor_mercado = "40,00 mill. €"

  #Métodos: 
  def correr (self):
    print("Correr")
  
  def lesionar (self):
    print("Lesionar")

  def __init__ (self):
    pass
    print("Constructor Equipo Napoli:")

hirvingLozano= EquipoNapoli()
print(hirvingLozano.nacionalidad)
print(hirvingLozano.equipo)
print(hirvingLozano.sexo)
print(hirvingLozano.posicion)
print(hirvingLozano.numero_dorsal)
print(hirvingLozano.nombre)
print(hirvingLozano.edad)
print(hirvingLozano.estatura)
print(hirvingLozano.peso)
print(hirvingLozano.valor_mercado)
hirvingLozano.patearBalon()
hirvingLozano.pasarBalon()
hirvingLozano.correr()
hirvingLozano.lesionar()
