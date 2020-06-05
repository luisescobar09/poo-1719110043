class Cadenas:
  
  repetir="S"
  while repetir=="S" or repetir=="s" :
    cadena=input("Escriba algo: ")
    print ("Carácteres de la cadena por separado:")
    for i in cadena:
      print(i)
    longitud = len(cadena) 
    print("Longitud de la cadena:",longitud)
    repetir=input("¿Desea analizar otra cadena s/n?:" )
