class Estudiante:

  #Atributos:
  escuela="UTEC Tulancingo"
  matricula = "1719110043"
  nacionalidad= "Mexicana"
  promedio = "9.7"
  documentos_personales = True

  #Métodos:
  def leer (self):
    print("Leer")

  def escribir (self):
    print("Escribir")

  def __init__ (self):
    pass
    print("Constructor Estudiante")

class EstudianteUtec(Estudiante):

  #Atributos:
  nombre = "José Luis Escobar Pérez"
  edad = "18 años"
  altura = "1.72 metros"
  peso = "65 kg."
  responsabilidad = True

  #Métodos:
  def sumar (self):
    print("Sumar")
  
  def restar (self):
    print("Restar")

  def leer (self):
    print("Leer de corrido")

  def escribir (self):
    print("Escribir con la mano izquierda")

  def __init__ (self):
    pass
    print("Constructor Estudiante Utec:")

estudianteJoseLuis= EstudianteUtec()
print(estudianteJoseLuis.escuela)
print(estudianteJoseLuis.matricula)
print(estudianteJoseLuis.nacionalidad)
print(estudianteJoseLuis.promedio)
print(estudianteJoseLuis.documentos_personales)
print(estudianteJoseLuis.nombre)
print(estudianteJoseLuis.edad)
print(estudianteJoseLuis.altura)
print(estudianteJoseLuis.peso)
print(estudianteJoseLuis.responsabilidad)
estudianteJoseLuis.leer()
estudianteJoseLuis.escribir()
estudianteJoseLuis.sumar()
estudianteJoseLuis.restar()
