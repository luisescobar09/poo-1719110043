class Estudiante:

  #Atributos:
  nombre = "José Luis Escobar Pérez"
  edad = "18 años"
  matricula = "1719110043"
  nacionalidad= "Mexicana"
  promedio = "9.7"
  altura = "1.72 metros"
  peso = "65 kg."
  documentos_personales = True
  responsabilidad = True
  honestidad = True

  #Métodos:
  def leer (self):
    print("Leer")

  def escribir (self):
    print("Escribir")
  
  def sumar (self):
    print("Sumar")
  
  def restar (self):
    print("Restar")
  
  def aprender (self):
    print("Aprender")

  def __init__ (self):
    print("Constructor Estudiante")

objeto_estudiante = Estudiante()

print("Atributos:")
print(objeto_estudiante.nombre)
print(objeto_estudiante.edad)
print(objeto_estudiante.matricula)
print(objeto_estudiante.nacionalidad)
print(objeto_estudiante.promedio)
print(objeto_estudiante.altura)
print(objeto_estudiante.peso)
print(objeto_estudiante.documentos_personales)
print(objeto_estudiante.responsabilidad)
print(objeto_estudiante.honestidad)

print("Métodos:")
objeto_estudiante.leer()
objeto_estudiante.escribir()
objeto_estudiante.sumar()
objeto_estudiante.restar()
objeto_estudiante.aprender()