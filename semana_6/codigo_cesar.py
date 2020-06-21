class RepetirProceso: #creamos una clase para el bucle

  def __init__(self): #agregamos el constructor
    pass

  def repetir(self): #creamos el método para el bucle
    repetir = "S" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s" : #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      
      class Cadena(RepetirProceso): #creamos la clase para las cadenas y heredamos la clase base (el bucle). Al ya existir un constructor en la clase base ya no es necesario en la clase hija

        cadena=input('Escribe algo:').lower()
        decidir=input("Desea cifrar o descifrar la cadena:").lower()
        clave=int(input("Cual es tu clave numerica (si lo deseas de forma descendente agrega - ):"))

        def cifrar_descifrar(self):
          if self.decidir=="cifrar":
            print("Tu cadena cifrada es:")
            for i in self.cadena:
              ascii=ord(i)
              caracter=chr(ascii+self.clave)
              final=caracter.replace("`","z").replace("{","a")
              print(final)

          else:
            print("Tu cadena descrifrada es:")
            for i in self.cadena:
              ascii=ord(i)
              print((chr(ascii+self.clave)))
      objeto = Cadena()  #creamos el objeto que llame a la clase
      objeto.cifrar_descifrar()

      repetir=input("¿Desea analizar otra cadena s/n? :") #preguntamos al usuario si quiere un nuevo analisis, si dice que si se repite el proceso hasta que diga que no

objetoBucle= RepetirProceso()  #creamos el objeto que llame a la clase
objetoBucle.repetir() #llamamos al método para que lo ejecute