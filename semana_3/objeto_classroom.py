class GoogleClassroom:

  #Atributos:
  interfaz = True
  asistente = True
  clases = True
  calendario = True
  registro = True

  #Métodos:
  def iniciarSesion (self):
    print("Iniciar sesión")

  def cerrarSesion (self):
    print("Cerrar sesión.")

  def __init__ (self):
    pass
    print("Constructor Google Classroom")

class Clase (GoogleClassroom): #se refiere a la clase de la materia
  #Atributos:
  codigo = True
  reuniones = True
  tablon = True
  comentarios = True
  participantes = True

  #Métodos: 
  def descargar (self):
    print("Descargar")

  def adjuntar (self):
    print("Adjuntar")
  
  def __init__ (self):
    pass
    print("Constructor Clase:")

materia= Clase() 
print(materia.interfaz)
print(materia.asistente)
print(materia.clases)
print(materia.calendario)
print(materia.registro)
print(materia.codigo)
print(materia.reuniones)
print(materia.tablon)
print(materia.comentarios)
print(materia.participantes)
materia.iniciarSesion()
materia.cerrarSesion()
materia.descargar()
materia.adjuntar()