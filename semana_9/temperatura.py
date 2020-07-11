class Temperaturas: #creamos una clase 
  temperaturas= [] #creamos las variables para almacenar los valores en los arreglos
  fechas=[]
  fecha_temp=[]
  archivos=()#creamos la variable para el txt
  def __init__(self): #agregamos el constructor
    pass

  def abrir_txt(self):#cremos el metodo para abrir el txt
    self.archivos = open("temperaturas.txt","a")#abrimos el archivo "txt" con "open" con el modo "a" para agregar información que escribamos

  def leer_repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      temperatura = float(input("Temperatura en °C: "))#pedimos que el usuario ingrese temperaturas
      fecha = input("Fecha de la temperatura: ")#pedimos que el usuario ingrese temperaturas
      self.fechas.append(fecha)
      self.temperaturas.append(temperatura)#almacenamos los valores ingresados en el arreglo
      datos=[temperatura,fecha]
      self.fecha_temp.append(datos)#almacenamos los valores ingresados en el arreglo
      repetir=input("¿Desea leer otra temperatura s/n? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no  

  def celsius(self):#creamos un método para los valores en el txt
    for f in range (len(self.fecha_temp)):#separamos cada valor ingresado
      self.archivos.write("Fecha: ")#titulo  
      fila= (self.fecha_temp[f][1])
      self.archivos.write(fila)#pidamos que se escriban los valores ingresados en el txt
      self.archivos.write("\n")#identifica el tipo de temperatura
      self.archivos.write("Temperatura °C: ")#titulo  
      fila= (self.fecha_temp[f][0])
      celsiustxt=str(fila)#convertimos de float a string
      self.archivos.write(celsiustxt)#pidamos que se escriban los valores ingresados en el txt
      self.archivos.write("°C \n")#identifica el tipo de temperatura
      self.archivos.write("Temperatura de °C a °F: ")#titulo 
      fahren= (fila*1.8)+32#hacemos el calculo de °C a °F
      fahrentxt=str(fahren)#convertimos de float a string
      self.archivos.write(fahrentxt)#pidamos que se escriban los valores ingresados en el txt
      self.archivos.write("°F \n")#identifica el tipo de temperatura
      self.archivos.write("\n")

  def promedios(self):#creamos método para valores en el txt
    suma=0#creamos una variable para el contador igualada a 0
    for i in self.temperaturas:#separamos cada valor ingresado
      suma += i#sumamos cada valor almacenado
    promedio = suma / len(self.temperaturas)#calculamos la suma de todos los valores entre el numero de vslores para promediar
    print("\nPromedio de las temperaturas:",promedio,"°C.")
    prom_fahren=(promedio*1.8)+32#convertimos el promedio a °F
    print("Promedio de las temperaturas en °F:",prom_fahren,"°F.")

  def temperatura_fecha_mayor(self):#creamos un método  
    mayor = 0#creamos una variable para hallar el mayor
    for i in self.temperaturas:#separamos cada valor ingresado
      if i > mayor:#comparamos cada numero hasta encontrar el mayor
        mayor = i#toma un nuevo valor hasta que encuentre el mayor
    print("Temperatura mayor:",mayor,"°C.")#imprimimos el numero mayor
    posicion=self.temperaturas.index(mayor)#buscamos la posicion del numero mayor con "index"
    fecha_temperatura=self.fechas[posicion]#el usuario ingresó una temperatura con su respectiva fecha, por lo tanto cada posicion está ordenada. Para encontrar la fecha de la temperatura mayor en el arreglo de fechas buscamos la posicion que le corresponde a esa fecha con la temperatura mayor.
    print("Fecha de la temperatura mayor:",fecha_temperatura)#imprimimos fecha 

  def cerrar_txt(self):#creamos método para cerrar el txt
    self.archivos.close()#con "close" cerramos el txt

objeto= Temperaturas()  #creamos el objeto que llame a la clase
objeto.abrir_txt()
objeto.leer_repetir() #llamamos a cada método para que se ejecute 
objeto.celsius()
objeto.promedios()
objeto.temperatura_fecha_mayor()
objeto.cerrar_txt()