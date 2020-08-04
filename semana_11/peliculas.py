class Peliculas: #creamos una clase 
  lista=[]#creamos variables para los arreglos
  nombre_lanzamiento=[]
  genero=[]
 
  def __init__(self): #agregamos el constructor
    pass

  def leer_repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      nombre_peli=input("\nIngrese nombre de la película: ")#pedimos nombre de la película
      genero_peli=(input("Ingresa genero: "))#pedimos su género
      lanzamiento_peli=int(input("Ingresa año de lanzamiento: "))#pedimos el año
      datos=[nombre_peli,genero_peli,lanzamiento_peli]#almacenamos los datos ingresados en esta variable
      self.lista.append(datos)#almacenamos los valores ingresados en el arreglo
      repetir=input("¿Desea leer otra película S/N? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no  

  def imprimir(self):#creamos un método para imprimir
    print("\nPelículas ingresadas:")
    for i in range(len(self.lista)):#leer cada valor con un ciclo FOR
      nombre=self.lista[i][0]#nombre es el primer dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición cero
      genero=self.lista[i][1]#genero es el segundo dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición uno
      lanzamiento=self.lista[i][2]#año es el tercer dato que pedimos que ingrese el usuario, por ello buscamos los valores en la posición dos
      print("\nNombre:",nombre)#imprimimos el nombre de cada película con su respectivo género y alño
      self.genero.append(genero)#almacenamos todos los generos ingresados en el arreglo
      print("Genero:",genero)
      #dato3=("Año lanzamiento:",lanzamiento)
      self.nombre_lanzamiento.append("\nNombre: "+nombre+"\nAño lanzamiento: "+str(lanzamiento))#guardamos nombre y año juntos poorque el diccionario solo permite dos valores
      print("Año lanzamiento:",lanzamiento)

  def generoPeli(self): #metodo de busqueda,almacenamiento y convertir a diccionario
    diccionario=dict(zip(self.nombre_lanzamiento,self.genero)) #con dict convertimos a diccionario y zip permite ingresar más de dos argumentos
    genero=input("\nIngresa el género de una pelicula: ") #ingresamos un género
    if genero in diccionario.values(): #con la función values leemos cada valor almacenado, si coincide con la variable continuamos
      print("\nPelículas del género "+genero+":")
      for i in diccionario: #leemos cada valor del diccionario
        if diccionario[i]==genero: #si tenemos el género imprimimos su nombre y año
          print(i)
    else:
      print("\nNo hay películas de género "+genero+".")#caso contrario imprimimos que no existe

objeto= Peliculas()  #creamos el objeto que llame a la clase
objeto.leer_repetir() #llamamos a cada método para que se ejecute
objeto.imprimir() 
objeto.generoPeli()