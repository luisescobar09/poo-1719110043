class Classroom:

  #Atributos:
  interfaz = True
  asistente = True
  clases = True
  codigo = True
  reuniones = True
  tablon = True
  comentarios = True
  participantes = True
  calendario = True
  registro = True

  #Métodos:
  def enviar (self):
    print("Enviar")

  def recibir (self):
    print("Recibir")
  
  def descargar (self):
    print("Descargar")
  
  def leer (self):
    print("Leer")
  
  def adjuntar (self):
    print("Adjuntar")

  def __init__ (self):
    print("Constructor Coche")

objeto_classroom = Classroom()

print("Atributos:")
print(objeto_classroom.interfaz)
print(objeto_classroom.asistente)
print(objeto_classroom.clases)
print(objeto_classroom.codigo)
print(objeto_classroom.reuniones)
print(objeto_classroom.tablon)
print(objeto_classroom.comentarios)
print(objeto_classroom.participantes)
print(objeto_classroom.calendario)
print(objeto_classroom.registro)

print("Métodos:")
objeto_classroom.enviar()
objeto_classroom.recibir()
objeto_classroom.descargar()
objeto_classroom.leer()
objeto_classroom.adjuntar()