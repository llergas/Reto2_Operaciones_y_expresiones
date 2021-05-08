# "Pollos Picochin"

# Importamos la librería datetime para poder ingresar fecha y hora a la factura.

from datetime import datetime

# En este programa pedimos la cedula para poder darle el nombre al archivo .txt y diferenciar de otros pedidos.

# Pedimos por consola los valores que deben tener las variables para procesar la información.


cedula = input("Ingrese la cedula del cliente: ")
nom = input("Ingrese el nombre del plato: ")
cant = int(input("Ingrese la cantidad de platos: "))
prec = float(input("Ingrese el precio por unidad: "))

# Con datetime.today el sistema me trae la fecha y la hora en que se ejecuta el programa.

fecha = datetime.today()
iva = (cant * prec)*0.19

# Utilizamos datos tipo bool ya que la propina es voluntaria. El cliente decide si la va a dar o no

prop = bool(int(input("Desea dar propina (Si = 1 / No = 0): ")))

# Utilizamos el valor de la variable prop (solo es falso (0) o verdadero(1) dependiendo de lo que decida el cliente)
# como un entero para poder determinar el valor de la propina si prop es True.

prop1 = prop * ((cant * prec)*0.20)

# Imprimimos los datos para que queden organizados y en forma de tabla

print("\n"*3)

# Utilizamos el comando .center() para poder centrar la impresión, en este caso lo centramos a 70 espacios

print("Asadero y Restaurante".center(70))
print("POLLOS PICOCHIN".center(70))
print("Nit. 92456951 - 8".center(70))

# Le damos el formato que queremos a la fecha en este caso escogimos día, mes, año y la hora fue horas, minutos y segundos.

print(fecha.strftime("%d/%m/%Y %H:%M:%S").center(70),"\n"*2)

# Utilizamos el comando .format() para poder hacer un encabezado con 4 columnas y sus respectivos nombres, además pueden
# contener hasta 15 espacios

print("{:^15}{:^15}{:^15}{:^15}".format("PLATO", "CANTIDAD","PRECIO UN", "TOTAL"))
print("{:^15}{:^15}{:^15}{:^15}".format(nom,cant,"$"+str(prec),"$"+str(cant*prec)))
print("____________________________________________________________________")
print("{:^15}{:^15}{:^15}{:^15}".format("Subtotal","","","$"+str(cant*prec)))
print("{:^15}{:^15}{:^15}{:^15}".format("IVA","","","$"+str(iva)))
print("{:^15}{:^15}{:^15}{:^15}".format("Total","","","$"+str(iva+(cant*prec))))
print("{:^15}{:^15}{:^15}{:^15}".format("Propina","","","$"+str(prop1)))
print("{:^15}{:^15}{:^15}{:^15}".format("Total","","","$"+str((iva+(cant*prec)+prop1))))

# Abrimos el archivo con nombre según el valor que tenga la variable cedula y lo abrimos en tipo escritura

file = open(f"picochin/{cedula}.txt", "w")

file.write(f"Fecha / Hora: {fecha} \n")
file.write(f"Nombre del plato: {nom} \n")
file.write(f"Numeros de platos: {cant} \n")
file.write(f"Precio del plato: {prec}\n\n")
file.write(f"Precio total: {cant * prec}\n")
file.write(f"IVA: {iva}\n")
file.write(f"Popina: {prop1}\n")
file.write(f"Total: {(cant * prec) + iva + prop1} \n")

file.close()



