class SerieTV:

  #Atributos:
  genero = "Caricatura"
  personaje = "Bob Esponja"
  nombre_capitulo = "El abismo"
  lugar_grabacion = "Estados Unidos"
  numero_capitulos = "225"
  estreno = "Temporada 13"
  maquillaje = True
  directores = True
  camaras = True
  fecha_lanzamiento = "1 de mayo 1999"

  #Métodos:
  def actuar (self):
    print("Actuar")

  def hablar (self):
    print("Hablar")
  
  def grabar (self):
    print("Grabar")
  
  def repetir (self):
    print("Repetir")
  
  def ver (self):
    print("Ver")

  def __init__ (self):
    print("Constructor Serie de TV")

objeto_serie = SerieTV()

print("Atributos:")
print(objeto_serie.genero)
print(objeto_serie.personaje)
print(objeto_serie.nombre_capitulo)
print(objeto_serie.lugar_grabacion)
print(objeto_serie.numero_capitulos)
print(objeto_serie.estreno)
print(objeto_serie.maquillaje)
print(objeto_serie.directores)
print(objeto_serie.camaras)
print(objeto_serie.fecha_lanzamiento)

print("Métodos:")
objeto_serie.actuar()
objeto_serie.hablar()
objeto_serie.grabar()
objeto_serie.repetir()
objeto_serie.ver()