class Banco:

  #Atributos:
  nombre = "BBVA"
  numero_ventanillas = "15 ventanillas"
  horario_atencion = "8:00 a.m a 4:00 p.m"
  color= "azul"
  cajeros_automaticos = True
  sitio_web = "bbva.mx"
  sucursal = "Pachuca Centro"
  direccion = "Calle Plaza de la Independencia 114, Centro, 42000 Pachuca de Soto, Hgo"
  gerente = True
  logotipo = True

  #Métodos:
  def depositar (self):
    print("Depositar")

  def retirar (self):
    print("Retirar")
  
  def pagar_servicios (self):
    print("Pagar servicios")
  
  def registrar_cuentas (self):
    print("Registrar cuentas")
  
  def consultar_saldo (self):
    print("Consultar saldo")

  def __init__ (self):
    print("Constructor Banco")

objeto_banco = Banco()

print("Atributos:")
print(objeto_banco.nombre)
print(objeto_banco.numero_ventanillas)
print(objeto_banco.horario_atencion)
print(objeto_banco.color)
print(objeto_banco.cajeros_automaticos)
print(objeto_banco.sitio_web)
print(objeto_banco.sucursal)
print(objeto_banco.direccion)
print(objeto_banco.gerente)
print(objeto_banco.logotipo)

print("Métodos:")
objeto_banco.depositar()
objeto_banco.retirar()
objeto_banco.pagar_servicios()
objeto_banco.registrar_cuentas()
objeto_banco.consultar_saldo()
