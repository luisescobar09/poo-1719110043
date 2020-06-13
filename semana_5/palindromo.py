class RepetirProceso: #creamos una clase para el bucle

  def __init__(self): #agregamos el constructor
    pass

  def repetir(self): #creamos el método para el bucle
    repetir = "S" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s" : #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      
      class Cadena(RepetirProceso): #creamos la clase para las cadenas y heredamos la clase base (el bucle). Al ya existir un constructor en la clase base ya no es necesario en la clase hija

        texto = input("Escribe algo:") #pedimos al usuario que escriba algo
        
        cadena = texto.lower().replace(",", "").replace(".", "").replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")#lower convierte todas las letras a minusculas y replace cambia una vocal con acento a sin acento, las "," "." y espacios los elimina, para que al final la cadena termine junta

        def palindromo(self): #creamos el método requerido
          igual, aux = 0, 0 #igualamos a 0 los contadores

          for i in reversed (range(0,len(self.cadena))): #el bucle for va a repetir sobre el rango de números, pero sera de forma invertida, usando reversed, usamos len para la longitud de la cadena y todo se almacenará en "i"
            print(i)
            if self.cadena[i].lower() == self.cadena[aux].lower(): #evaluar si el carácter ubicado en "i" de la variable cadena es igual al carácter ubicado en el índice "aux" en la variable cadena. 
              igual += 1#si cumple la condicion almacena el resultado
            aux += 1#si no la cumple, se almacena aquí
          if len(self.cadena) == igual: #evalua si la longitud de la cadena es igual al valor que tiene la variable igual
            print ("La cadena es palíndromo.")#imprime esto si es verdadera
          else:
            print("La cadena no es palíndromo.")#caso contrario imprime lo contrario

        def espacios(self):
              espacio = self.texto.count(" ") #la funcion count representa la cantidad de apariciones de una subcadena (en este caso los espacios) dentro de la cadena 
              print("No. espacios en la cadena:",espacio)  

        def vocales(self):
            a = self.cadena.count("a") #la funcion count representa la cantidad de apariciones de una subcadena (en este caso las vocales) dentro de la cadena 
            e = self.cadena.count("e")
            i = self.cadena.count("i")
            o = self.cadena.count("o")
            u = self.cadena.count("u")
            print("No. vocales en la cadena:",a+e+i+o+u)#hacemos la suma para obtener el resultado total

      objeto = Cadena()  #creamos el objeto que llame a la clase
      objeto.palindromo() #llamamos a los métodos
      objeto.espacios()
      objeto.vocales()
      
      repetir=input("¿Desea analizar otra cadena s/n? :") #preguntamos al usuario si quiere un nuevo analisis, si dice que si se repite el proceso hasta que diga que no

objetoBucle= RepetirProceso()  #creamos el objeto que llame a la clase
objetoBucle.repetir() #llamamos al método para que lo ejecute