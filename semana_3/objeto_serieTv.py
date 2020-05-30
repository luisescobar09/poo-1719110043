class SerieTv:

  #Atributos:
  genero = "Caricaturas"
  lugar_grabacion = "Estados Unidos"
  maquillaje = True
  directores = True
  camaras = True

  #Métodos:
  def actuar (self):
    print("Actuar")

  def hablar (self):
    print("Hablar")

  def __init__ (self):
    pass
    print("Constructor Serie TV")

class Caricaturas(SerieTv):

  #Atributos:
  personaje = "Bob Esponja"
  nombre_capitulo = "El abismo"
  estreno = "Temporada 13"
  numero_capitulos = "225"
  fecha_lanzamiento = "1 de mayo 1999"

  #Métodos: 
  def repetir (self):
    print("Repetir")
  
  def ver (self):
    print("Ver")

  def __init__ (self):
    pass
    print("Constructor Caricaturas:")

bobEsponja= Caricaturas()
print(bobEsponja.genero)
print(bobEsponja.lugar_grabacion)
print(bobEsponja.maquillaje)
print(bobEsponja.directores)
print(bobEsponja.camaras)
print(bobEsponja.personaje)
print(bobEsponja.nombre_capitulo)
print(bobEsponja.estreno)
print(bobEsponja.numero_capitulos)
print(bobEsponja.fecha_lanzamiento)
bobEsponja.actuar()
bobEsponja.hablar()
bobEsponja.repetir()
bobEsponja.ver()
