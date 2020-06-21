class RepetirProceso: #creamos una clase para el bucle

  def __init__(self): #agregamos el constructor
    pass

  def repetir(self): #creamos el método para el bucle
    repetir = "S" #creamos la variable a evaluar
    while repetir=="S" or repetir=="s" : #mientras cumpla la condicion, todo lo que esté adentro se cumplirá
      
      class Cadena(RepetirProceso): #creamos la clase para las cadenas y heredamos la clase base (el bucle). Al ya existir un constructor en la clase base ya no es necesario en la clase hija
        cadena=input('Escribe algo:').lower().replace(",", "").replace(".", "").replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")#lower convierte todas las letras a minusculas y replace cambia una vocal con acento a sin acento, las "," "." y espacios los elimina, para que al final la cadena termine junta
        decidir=input("¿Desea cifrar o descifrar la cadena? ").lower()#pedimo qué desea hacer
        clave=int(input("¿Cuál es tu clave numerica? "))#pedimos un número de clave
        def cifrar_descifrar(self): #creamos el método requerido
          if self.clave>26: #si es mayor la clave a 26cancelamos lo demas
            print("Pasaste el número máximo de letras del abecedario, intenta de nuevo.")
          else: #caso contrario
            if self.decidir=="cifrar": #si decide cifrar
              print("Tu cadena cifrada es:")
              for i in self.cadena: #creamos un FOR para separar cada caracter
                ascii=ord(i) #lo convertimos a codigo ascii
                caracter=chr(ascii+self.clave)#al numero en codigo ascii le sumamos el valor de la clave y lo convertimos de nuevo a caracter
                final=caracter.replace(chr(123),"a").replace(chr(124),"b").replace(chr(125),"c").replace(chr(126),"d").replace(chr(127),"e").replace(chr(128),"f").replace(chr(129),"g").replace(chr(130),"h").replace(chr(131),"i").replace(chr(132),"j").replace(chr(133),"k").replace(chr(134),"l").replace(chr(135),"m").replace(chr(136),"n").replace(chr(267),"ñ").replace(chr(266),"m").replace(chr(265),"l").replace(chr(264),"k").replace(chr(263),"j").replace(chr(262),"i").replace(chr(261),"h").replace(chr(260),"g").replace(chr(259),"f").replace(chr(258),"e").replace(chr(257),"d").replace(chr(256),"c").replace(chr(255),"b").replace(chr(254),"a").replace(chr(253),"z").replace(chr(252),"y").replace(chr(251),"x").replace(chr(250),"w").replace(chr(249),"v").replace(chr(248),"u").replace(chr(247),"t").replace(chr(246),"s").replace(chr(245),"r").replace(chr(244),"q").replace(chr(243),"p").replace(chr(242),"o").replace(chr(137),"o").replace(chr(138),"p").replace(chr(139),"q").replace(chr(140),"r").replace(chr(141),"s").replace(chr(142),"t").replace(chr(143),"u").replace(chr(144),"v").replace(chr(145),"w").replace(chr(146),"x").replace(chr(147),"y").replace(chr(148),"z") #agregamos las conversiones a partir de la z hacia adelante 26, ademas la ñ
                print(final) #imprimimos el resultado

            else: #caso contrario, desciframos
              print("Tu cadena descrifrada es:")
              for i in self.cadena: #creamos un FOR para separar cada caracter
                ascii=ord(i) #lo convertimos a codigo ascii
                caracter=chr(ascii-self.clave)#al numero en codigo ascii le restamos el valor de la clave y lo convertimos de nuevo a caracter
                final=caracter.replace(chr(71),"a").replace(chr(72),"b").replace(chr(73),"c").replace(chr(74),"d").replace(chr(75),"e").replace(chr(76),"f").replace(chr(77),"g").replace(chr(78),"h").replace(chr(79),"i").replace(chr(80),"j").replace(chr(81),"k").replace(chr(82),"l").replace(chr(83),"m").replace(chr(84),"n").replace(chr(85),"o").replace(chr(86),"p").replace(chr(87),"q").replace(chr(88),"r").replace(chr(89),"s").replace(chr(90),"t").replace(chr(91),"u").replace(chr(92),"v").replace(chr(93),"w").replace(chr(94),"x").replace(chr(95),"y").replace(chr(96),"z").replace(chr(215),"ñ").replace(chr(216),"n").replace(chr(217),"m").replace(chr(219),"l").replace(chr(218),"k").replace(chr(219),"j").replace(chr(220),"i").replace(chr(221),"h").replace(chr(222),"g").replace(chr(223),"f").replace(chr(224),"e").replace(chr(225),"d").replace(chr(226),"c").replace(chr(227),"b").replace(chr(228),"a").replace(chr(229),"z").replace(chr(230),"y").replace(chr(231),"x").replace(chr(232),"w").replace(chr(233),"v").replace(chr(234),"u").replace(chr(235),"t").replace(chr(236),"s").replace(chr(237),"r").replace(chr(238),"q").replace(chr(239),"p").replace(chr(240),"o")#agregamos las conversiones a partir de la a en retroceso 26, ademas la ñ
                print(final)#imprimimos el resultado

      objeto = Cadena()  #creamos el objeto que llame a la clase
      objeto.cifrar_descifrar()#llamamos al método

          
      repetir=input("¿Desea cifrar/descifrar otra cadena s/n? : ")#preguntamos al usuario si quiere un nuevo analisis, si dice que si se repite el proceso hasta que diga que no

objetoBucle= RepetirProceso()  #creamos el objeto que llame a la clase
objetoBucle.repetir() #llamamos al método para que lo ejecute