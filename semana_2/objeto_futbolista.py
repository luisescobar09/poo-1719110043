class Futbolista:

  #Atributos:
  nombre = "Hirving Lozano"
  nacionalidad = "Mexicana"
  edad = "24 años"
  equipo = "SC Napoli"
  sexo = "Masculino"
  posicion = "extremo izquierdo o derecho"
  numero_dorsal = "11"
  estatura = "1.74 metros"
  peso = "72 kg."
  valor_mercado = "40,00 mill. €"

  #Métodos:
  def patear (self):
    print("Patear un balón")

  def pasar (self):
    print("Pasar un balón")
  
  def cabecear (self):
    print("Cabecear")
  
  def correr (self):
    print("Correr")
  
  def lesionar (self):
    print("Lesionar")

  def __init__ (self):
    print("Constructor Serie de TV")

objeto_futbolista = Futbolista()

print("Atributos:")
print(objeto_futbolista.nombre)
print(objeto_futbolista.nacionalidad)
print(objeto_futbolista.edad)
print(objeto_futbolista.equipo)
print(objeto_futbolista.sexo)
print(objeto_futbolista.posicion)
print(objeto_futbolista.numero_dorsal)
print(objeto_futbolista.estatura)
print(objeto_futbolista.peso)
print(objeto_futbolista.valor_mercado)

print("Métodos:")
objeto_futbolista.patear()
objeto_futbolista.pasar()
objeto_futbolista.cabecear()
objeto_futbolista.correr()
objeto_futbolista.lesionar()