class Banco:

  #Atributos:
  nombre = "BBVA"
  color= "azul"
  cajeros_automaticos = True
  sitio_web = "bbva.mx"
  logotipo = True

  #Métodos:
  def depositar (self):
    print("Depositar")

  def retirar (self):
    print("Retirar")

  def __init__ (self):
    pass
    print("Constructor Banco")

class BbvaSucursal(Banco):

  #Atributos:
  sucursal = "Pachuca Centro"
  direccion = "Calle Plaza de la Independencia 114, Centro, 42000 Pachuca de Soto, Hgo"
  numero_ventanillas = "15 ventanillas"
  horario_atencion = "8:00 a.m a 4:00 p.m"
  gerente = True

  #Métodos:
  def pagarServicios (self):
    print("Pagar servicios")
  
  def registrarCuentas (self):
    print("Registrar cuentas")

  def __init__ (self):
    pass
    print("Constructor BBVA Sucursal")

bbvaPachuca= BbvaSucursal()
print(bbvaPachuca.nombre)
print(bbvaPachuca.color)
print(bbvaPachuca.cajeros_automaticos)
print(bbvaPachuca.sitio_web)
print(bbvaPachuca.logotipo)
print(bbvaPachuca.sucursal)
print(bbvaPachuca.direccion)
print(bbvaPachuca.numero_ventanillas)
print(bbvaPachuca.horario_atencion)
print(bbvaPachuca.gerente)
bbvaPachuca.depositar()
bbvaPachuca.retirar()
bbvaPachuca.pagarServicios()
bbvaPachuca.registrarCuentas()
