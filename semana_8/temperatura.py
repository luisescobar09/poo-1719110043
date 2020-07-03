class RepetirProceso: #creamos una clase para el bucle
  temperaturas= []
  archivos = open("temperaturas.txt","r")
  def __init__(self): #agregamos el constructor
    pass
  
  def repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      temperatura = float(input("Temperatura en °C:")).write("temperaturas.txt")
      self.temperaturas.append(temperatura)
      repetir=input("¿Desea leer otra temperatura s/n? : ")#preguntamos al usuario si quiere un nuevo analisis, si dice que si se repite el proceso hasta que diga que no  

  def fahrenheit(self):
    for f in self.temperaturas:
      fahren= (f*1.8)+32
      return fahren

  def promedio(self):
    suma=0
    for i in self.temperaturas:
        suma += i
    prom = suma / len(self.temperaturas)
    return prom

objeto= RepetirProceso()  #creamos el objeto que llame a la clase
objeto.repetir() #llamamos al método para que lo ejecute 
print("Temperatura en °F",objeto.fahrenheit())

print("Promedio",objeto.promedio())