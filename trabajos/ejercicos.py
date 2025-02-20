age = int(input("Escribe tu edad "))
print("")
height = float(input("Escribe tu altura "))
print("")
##3
complex = complex(input("Un numero complejo "))

##4 Triangle
print("")
base = int(input("Ingresa la base de tiengulo "))
heightT = int(input("Ingresa la altura del triangulo "))
area = float((base * heightT)/2)
print("El area de tu triangulo es: ", area)

##5 Perimeter
print("")
lado1 = int(input("El primer lado es: "))
lado2 = int(input("El segundo lado es: "))
lado3 = int(input("El tercer lado es: "))
perimeter = lado1 + lado2 + lado3
print("El perimetro del triangulo es de: ", perimeter)

##6 Length and Width
print("")
Length = int(input("Ingresa el valor del largo: ")) ##Largo
Width = int(input("Ingresa el valor del ancho: ")) #Ancho
area1 = Length * Width
perimeter1 = 2 * (Length + Width)
print("El perimetro es de: ", perimeter1)

##7 Radius
print("")
radius = float(input("Ingresa la circunferencia de tu circulo: "))
pi = float(3.1416)
areac = float(pi * radius * radius)
circunference = float(2 * pi * radius)
print("Tu area es de: ", areac)
print("Tu circunferencia es de: ", circunference)

##8 Slope
print("")
print("Interaccion de la pendiente:")
pendiente = 2
intY = -2
intX = intY
pen = ((pendiente * intX) + intY)
print("La interacción es de: ", pen) 

##9 Euclidean distance
print("")
x = (2,2)
y = (6,10)
m = y/x
print(m)