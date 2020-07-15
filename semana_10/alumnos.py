class Temperaturas: #creamos una clase 
  temperaturas= [] #creamos las variables para almacenar los valores en los arreglos
  datos_txt=[]
  datos=[]
  lista=[]
  archivos=()
  def __init__(self): #agregamos el constructor
    pass

  def leer_repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      nombre=input("Ingrese nombre: ")#pedimos nombre del alumno
      edad=2020-int(input("Ingresa año de nacimiento: "))#pedimos año de nacimiento y para calcular la edad le restamos al año actual (2020) el año de nacimiento del alumno
      grupo=input("Ingresa grupo: ")#pedimos el grupo del alumno
      datos=[nombre,edad,grupo]
      self.lista.append(datos)#almacenamos los valores ingresados en el arreglo
      repetir=input("¿Desea ingresar otro alumno s/n? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no  

  def imprimir(self):#creamos un método para imprimir
    for i in range(len(self.lista)):
      nombre=self.lista[i][0]#nombre es el primer dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición cdro
      edad=self.lista[i][1]#edad es el segundo dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición uno
      print("\nNombre:",nombre,)#imprimimos el nombre de cada alumno con su respectiva edad
      print("Edad:",edad,"años.")

  def abrir_txt(self):#cremos el metodo para abrir el txt
    self.archivos = open("alumnos.txt","r")#abrimos el archivo "txt" con "open" con el modo "a" para agregar información que escribamos
    print("\nEjemplo con txt:\n")

  def leer_archivo(self):
    for j in self.archivos:
      fila=j.replace("Nombre: ","").replace(" año nacimiento: ","").replace(" grupo: ","").replace("\n","").split(",")#con replace eliminamos caracteres innecesarios para cada varaible, como sus títulos; usamos split para dividir cada valor cuando aparezca una ","
      self.datos_txt.append(fila)#almacenamos lo obtenido en una lista

  def imprimir_archivo(self):#creamos un método para imprimir
    for i in range(len(self.datos_txt)):
      nombre=self.datos_txt[i][0]#nombre es el primer dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición cdro
      edad=int(self.datos_txt[i][1])#edad es el segundo dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición uno
      print("Nombre:",nombre,)#imprimimos el nombre de cada alumno con su respectiva edad
      print("Edad:",2020-edad,"años.")

  def cerrar_txt(self):#creamos método para cerrar el txt
    self.archivos.close()#con "close" cerramos el txt

objeto= Temperaturas()  #creamos el objeto que llame a la clase
objeto.leer_repetir() #llamamos a cada método para que se ejecute
objeto.imprimir() 
objeto.abrir_txt()
objeto.leer_archivo()
objeto.imprimir_archivo()
objeto.cerrar_txt()
