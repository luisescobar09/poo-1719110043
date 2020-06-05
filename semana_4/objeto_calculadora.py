class Calculadora:

  #Atributos:
  funciones = True
  memoria = True
  exponente = True
  marca = "Casio"
  tipo_calculadora = "Cientifica"

  #Métodos:
  def sumar (self):
    print("Sumar")

  def restar (self):
    print("Restar")
  
  def __init__ (self):
    pass
    print("Constructor Calculadora")

class Casio(Calculadora):

  #Atributos:
  digitos_max = "14"
  costo = "275 pesos"
  tamano = "Mediana"
  peso = "512 gramos"
  sonido = False

  #Métodos: 
  def multiplicar (self):
    print("Multiplicar")
  
  def dividir (self):
    print("Dividir")

  def sumar (self):
    print("Sumar con parentesis, corchetes, llaves")

  def restar (self):
    print("Restar fracciones")

  def __init__ (self):
    
    pass
    print("Constructor Casio:")

fx300ESPlus= Casio()
print(fx300ESPlus.funciones)
print(fx300ESPlus.memoria)
print(fx300ESPlus.exponente)
print(fx300ESPlus.marca)
print(fx300ESPlus.tipo_calculadora)
print(fx300ESPlus.digitos_max)
print(fx300ESPlus.costo)
print(fx300ESPlus.tamano)
print(fx300ESPlus.peso)
print(fx300ESPlus.sonido)
fx300ESPlus.sumar()
fx300ESPlus.restar()
fx300ESPlus.multiplicar()
fx300ESPlus.dividir()
