class Calculadora:

  #Atributos:
  funciones = True
  memoria = True
  digitos_max = "12"
  sonido = False
  exponente = True
  marca = "Casio"
  tipo_calculadora = "Cientifica"
  costo = "165 pesos"
  tamano = "Mediana"
  peso = "512 gramos"

  #Métodos:
  def sumar (self):
    print("Sumar")

  def restar (self):
    print("Restar")
  
  def multiplicar (self):
    print("Multiplicar")
  
  def dividir (self):
    print("Dividir")
  
  def encender (self):
    print("Encender")

  def __init__ (self):
    print("Constructor Coche")

objeto_calculadora = Calculadora()

print("Atributos:")
print(objeto_calculadora.funciones)
print(objeto_calculadora.memoria)
print(objeto_calculadora.digitos_max)
print(objeto_calculadora.sonido)
print(objeto_calculadora.exponente)
print(objeto_calculadora.marca)
print(objeto_calculadora.tipo_calculadora)
print(objeto_calculadora.costo)
print(objeto_calculadora.tamano)
print(objeto_calculadora.peso)

print("Métodos:")
objeto_calculadora.sumar()
objeto_calculadora.restar()
objeto_calculadora.multiplicar()
objeto_calculadora.dividir()
objeto_calculadora.encender()