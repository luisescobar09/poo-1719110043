class Temperaturas: #creamos una clase para el bucle
  temperaturas= [] #creamos la variable para almacenar los valores del arreglo
  archivos = open("temperaturas.txt","a")#abrimos el archivo "txt" con "open" con el modo "a" para agregar información que escribamos

  def __init__(self): #agregamos el constructor
    pass
  
  def leer_repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      temperatura = float(input("Temperatura en °C: "))#pedimos que el usuario ingrese temperaturas
      self.temperaturas.append(temperatura)#almacenamos los valores ingresados en el arreglo
      repetir=input("¿Desea leer otra temperatura s/n? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no  

  def celsius(self):#creamos un método para los valores en el txt
    self.archivos.write("Temperaturas en °C: \n")#titulo 
    for c in self.temperaturas:#separamos cada valor ingresado
      celsiustxt=str(c)#convertimos de float a string
      self.archivos.write(celsiustxt)#pidamos que se escriban los valores ingresados en el txt
      self.archivos.write("°C \n")#identifica el tipo de temperatura
      

  def fahrenheit(self):#creamos un método para los valores en el txt
    self.archivos.write("Temperaturas de °C a °F: \n")#titulo 
    for f in self.temperaturas:#separamos cada valor ingresado
      fahren= (f*1.8)+32#hacemos el calculo de °C a °F
      fahrentxt=str(fahren)#convertimos de float a string
      self.archivos.write(fahrentxt)#pidamos que se escriban los valores ingresados en el txt
      self.archivos.write("°F \n")#identifica el tipo de temperatura

  def promedio_celsius(self):#creamos método para valores en el txt
    suma=0#creamos una variable para el contador igualada a 0
    self.archivos.write("Promedio de las temperaturas en °C: \n")#titulo
    for i in self.temperaturas:#separamos cada valor ingresado
      suma += i#sumamos cada valor almacenado
    promedio = suma / len(self.temperaturas)#calculamos la suma de todos los valores entre el numero de vslores para promediar
    promedio_txt=str(promedio)#convertimos de float a string
    self.archivos.write(promedio_txt)#pedimos que se escriban los valores ingresados en el txt
    self.archivos.write("°C \n")#identificamos el tipo de temperatura
  
  def promedio_fahren(self):
    self.archivos.write("Promedio de las temperaturas en °F: \n" )#creamos método para los valores en el txt
    suma=0#creamos una variable para el contador igualada a 0
    for i in self.temperaturas:#separamos cada valor ingresado
      suma+= i#sumamos cada valor almacenado
    promedio = suma / len(self.temperaturas)#calculamos la suma de todos los valores entre el numero de vslores para promediar
    prom_fahren=(promedio*1.8)+32#convertimos el promedio a °F
    promedio_txt=str(prom_fahren)#convertimos de float a string
    self.archivos.write(promedio_txt)#pedimos que se escriban los valores ingresados en el txt
    self.archivos.write("°F \n")#identificamos el tipo de temperatura

  def cerrar_archivo(self):#creamos método para cerrar el txt
    self.archivos.close()#con "close" cerramos el txt

objeto= Temperaturas()  #creamos el objeto que llame a la clase
objeto.leer_repetir() #llamamos a cada método para que se ejecute 
objeto.celsius()
objeto.fahrenheit()
objeto.promedio_celsius()
objeto.promedio_fahren()
objeto.cerrar_archivo()