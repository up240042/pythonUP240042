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
Width = int(input("Ingresa el valor del ancho: ")) ##Ancho
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
pendiente = 2 ##la pendiente  de la ecuacion
intY = -2     ##Interaccion con eje y
intX = intY / pendiente  ##Interaccion con eje x
print("La pendiente de la ecuacion es: ", pendiente)
print("La interacción es de: ", intX) 

##9 Euclidean distance
print("")
x1 = 2
x2 = 6
y1 = 2
y2 = 10
distance = ((x2 - x1)**2 + (y2-y1)**2)**0.5
print("La distancia entre los dos puntos es: ", distance)
slope = (y2 - y1) / (x2 - x1)
print("The slope is: ", slope)

##10 Compare
print("")
Compare = pendiente <= slope
print("La diferencia entre las pendientes es de: ", Compare)

##11 Value Y
print("")
vaX = int(input("Ingresa el valor de X "))
vaY = (vaX**2 + (6 * vaX) + 9) 
print("El valor de la variable Y es igual a ", "|", vaY, "|")

##12
print("")
##python = int(input("Ingresa el valor de python "))
##dragon = int(input("Ingresa el valor de dragon "))
python = 5
dragon = 3
comp = python == dragon
print("La comparación de los numeros fue: ", comp)