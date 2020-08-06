class Excepciones: #creamos una clase 
  lista=[]#creamos variable para el arreglo
  numero=()
  indice=()
  import math #importamos para la raíz

  def __init__(self): #agregamos el constructor
    pass

  def leer_repetir(self): #creamos el método para el bucle
    repetir = "s" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      try: #intenta comprobar que sea correcto
        numero=int(input("\nIngresa un número: "))#pedimos un número
        self.lista.append(numero)#almacenamos los valores en la lista
      except Exception as error: #si hay un error del usuario
        print("Datos erroneos, favor de verificar.")
      repetir=input("¿Desea ingresar otro número S/N? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no

  def index(self):#creamos el método para el indice
    try:#intenta comprobar que sea correcto
      self.indice=int(input("\nIngresa un índice para realizar las sig. acciones: "))
      try:#intenta comprobar que sea correcto
        self.numero=self.lista[self.indice]#localizamos la posicion que ingresó el usuaeio dentro de la lista
        print("\nNúmero de la lista en la posición",self.indice,":",self.numero)
      except Exception as error:#si hay un error del usuario
        print("Datos erroneos, favor de verificar.")
    except Exception as error:#si hay un error del usuario
      print("Datos erroneos, favor de verificar") 

  def parNon(self):#creamos un método para saber si es par o impar
    try:#intenta comprobar que sea correcto
      self.numero=self.lista[self.indice]#localizamos la posicion que ingresó el usuaeio dentro de la lista
      if self.numero % 2 ==0:#una regla de un número par dice que si el residuo de cualquier número dividido entre dos es igual a cero, es par
        print("El número",self.numero,"es par")
      else:#caso contrario es impar
        print("El número",self.numero,"es impar")
    except Exception as error:#si hay un error del usuario
      error=("Datos erroneos, favor de verificar.")

  def raiz(self):#creamos un método para calcular la raíz
    try:#intenta comprobar que sea correcto
      self.numero=self.lista[self.indice]#localizamos la posicion que ingresó el usuaeio dentro de la lista
      if self.numero>=0:#cualquier número mayor o igual a cero puede tener raíz
        print("Raíz cuadrada de",self.numero,":",self.math.sqrt(self.numero))#con math.sqrt calculamos la raíz
      else: #caso contrario no tienen (números negativos)
        print("Números negativos no tienen raíz.")
    except Exception as error:#si hay un error del usuario
      error=("Datos erroneos, favor de verificar.")

  def cubo(self):#creamos un método para calcular el número elevado al cubo
    try:#intenta comprobar que sea correcto
      self.numero=self.lista[self.indice]#localizamos la posicion que ingresó el usuaeio dentro de la lista
      cubo=pow(self.numero, 3)#funcion pow eleva a la potencia que le asignes (3 en este caso)
      print("Número",self.numero,"elevado al cubo:",cubo)
    except Exception as error:#si hay un error del usuario
      error=("Datos erroneos, favor de verificar.")

objeto= Excepciones()  #creamos el objeto que llame a la clase
objeto.leer_repetir() #llamamos a cada método para que se 
repetir = "s" #creamos la variable a evaluar
while repetir=="S" or repetir=="s": #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
  objeto.index()#metemos los métodos dentro del bucle por si hay una respuesta afirmativa por si quiere calcular de nuevo
  objeto.parNon()
  objeto.raiz()
  objeto.cubo()

  repetir=input("\n¿Desea realizar otro calculo con otro indice S/N? : ")#preguntamos al usuario si requiere una nueva lectura, si dice que si se repite el proceso hasta que diga que no