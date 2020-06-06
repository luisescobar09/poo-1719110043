class RepetirProceso: #creamos una clase para el bucle

  def __init__(self): #agregamos el constructor
    pass

  def repetir(self): #creamos el método para el bucle
    repetir = "S" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s" : #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
    
      class Cadena(RepetirProceso): #creamos la clase para las cadenas y heredamos la clase base (el bucle). Al ya existir un constructor en la clase base ya no es necesario en a clase hija

        cadena = input("Escribe algo:") #pedimos al usuario que escriba algo 

        def separar(self): #creamos el método requerido
          print ("Carácteres de la cadena por separado:") #imprimimos la instrucción
          for i in self.cadena: #colocamos un ciclo FOR para que lea cada carácter 
            print(i) #imprimimos la variable "i" que leyó cada carácter y aparezca en lista

        def tipoDato(self): #creamos el método requerido
          print ("Tipo de dato por cada carácter:") #imprimimos la instrucción
          for i in self.cadena: #colocamos un ciclo FOR para que lea cada carácter
            print(i,": ",type (i)) #imprimimos la variable "i" que leyó cada carácter y aparezca en lista y, agregamos la funcion "type" para que imprima el tipo de dato en cada cáracter.

      objeto = Cadena()  #creamos el objeto que llame a la clase
      objeto.separar() #llamamos al método para que lo ejecute
      objeto.tipoDato() #llamamos al método para que lo ejecute
      print("Longitud de la cadena:",len(objeto.cadena)) #imprimimos la longitud de la cadena con la función "len"
      print("Longitud de la cadena sin espacios:",len(objeto.cadena.strip())) #imprimimos la longitud de la cadena con la función "len" y sin espacios agregamos "strip"

      repetir=input("¿Desea analizar otra cadena s/n?:" ) #preguntamos al usuario si quiere un nuevo analisis, si dice que si se repite el proceso hasta que diga que no

objetoBucle= RepetirProceso()  #creamos el objeto que llame a la clase
objetoBucle.repetir() #llamamos al método para que lo ejecute