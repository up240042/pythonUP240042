## 1 Concatenate
fir = "Thirty_"
sec = "days_"
ter = "of_"
cuar = "python"
Comp = fir  + sec + ter + cuar
print(Comp)

## 2 
print("")
fir1 = "coding "
sec1 = "fot "
ter1 = "all"
comp1 = fir1 + sec1 + ter1
print(comp1)

## *3 - 4
print("")
company = "Full "
com2 = company + comp1 


## 3 - *4
print("")
print(com2)

## 5
print("")
len(com2)
print(len(com2))

## 6
print("")
may = com2.upper() ##Convierte minisculas en mayusculas
print(may)

## 7
print("")
men = com2.lower()
print(men)

## 8
print("")
cap = com2.capitalize()
ti = com2.title()
swa = com2.swapcase()
print("*" ,cap)
print("*", ti)
print("*", swa)

## 9
print("")
print("Ejercicio 9")
Cu = "Coding For All"
op = Cu.strip("All")

print(op)

## 10 
print("")
hol = "Coding For All"
sub = "For"
print(hol.index(sub))
print()

## 11 
print("")
print("Ejercicio 11")
cod = "Coding For All"
rem = cod.replace("Coding", "Hola") ##Poner la palabra a remplazar y la nueva
print("Se Remplazo la palabra Coding," , rem)

## 12 
print("")
print("Ejercicio 12")
cod1 = "Python for Everyone"
print(cod1)
rem = cod1.replace("Everyone" , "All")
print("Palabra nueva:  ", rem)

## 13
print("")
print("Ejercicio 13")
se = rem.split() ##Divide la palabra
print(se)

## 14
print("")
print("Ejercicio 14")
app = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
se1 = app.split(",") # Separa usando la coma seguida de un espacio
print(se1)

## 15 
print("")
print("Ejercicio 15")
co = "Coding For All"
se2 = co.split() #Divide la oracion rn partes
se3 = se2.index("Coding") #encuentra el valor de la posicion de la palabra indicada
print(se3)

co = "Coding For All"
se2 = co[0] # Indica la letra en esa posicion
print(se2)

## 16
print("")
print("Ejercicio 16")
co = "Coding For All"
se4 = co.split()
se5 = se4.index("All")
print(se5)

co = "Coding_For_All"
se4 = co[13]
print(se4)

## 17
print("")
print("Ejercicio 17")
co = "Coding For All"
se4 = co[10]
print("El valor de la posicion es: ")
print(se4)

# 18
print("")
print("Ejercicio 18")
pfe= "Python For Everyone"
con = pfe[0] 
con1 = pfe[7] 
con2 = pfe[11]
print(con + con1 + con2)

# 19
print("")
print("Ejercicio 19")
n = print("Coding For All")
n =  pfe[0] + pfe[7] +  pfe[11]
print(n)

# 20
print("")
print("Ejercicio 20")
nex = "Coding For All"
print(nex)
ocu = nex.find("C") #Encuentra el la primera posicion de la letra
print(ocu)

# 21
print("")
print("Ejercicio 21")
print(nex)
oco = nex.find("F")
print(oco)

# 22
print("")
print("Ejercicio 22")
nox = "Coding For All"
print("Ultima aparicion de:", "l en ", nox)
ul = nox.rfind("l") #Encuentra la ultima vez que una letra aparecio
print(ul)

# 23
print("")
print("Ejercicio 23")
sen = "You cannot end a sentence with because because because is a conjunction"
print("Primera aparicion de", "because en:", sen)
bea = sen.find("beacause")
print(bea)

# 24
print("")
print("Ejercicio 24")
sen1 = "You cannot end a sentence with because because because is a conjunction"
print("Ultima aparicion de", "because en:", sen1)
bea1 = sen1.rfind("beacause")
print(bea1)

# 25
print("")
print("Ejercicio 25")
tex = "You cannot end a sentence with because because because is a conjunction"
print(tex)
cor = tex.replace("because because because", "")
print(cor)

# 26
print("")
print("Ejercicio 26")
tex1= "You cannot end a sentence with because because because is a conjunction"
print(tex1)
enc = tex1.find("because")
enco = tex1.index("because")
print(enc)
print(enco)

# 27
print("")
print("Ejercicio 27")
tex = "You cannot end a sentence with because because because is a conjunction"
print(tex)
cor = tex.replace("because because because", "")
print(cor)  

# 28
print("")
print("Ejercicio 28")
print("¿'Coding For All' comienza con una subcadena Coding?")
tcod = "Coding For All"
#print(tcod)
codi = tcod.startswith("Coding") #Revisa si la cadena comineza con la palabra ingresada
print(codi)

# 29
print("")
print("Ejercicio 29")
print("¿'Coding For All' termina con una codificación de subcadena?")
tcod = "Coding For All"
cod2 = tcod.endswith("Coding") #Revisa si la cadena termina con la palabra ingresada
print(cod2)

# 30
print("")
print("Ejercicio 30")
print("Elimina los espacios en la oracion: '   Coding For All      '")
espa = "   Coding For All      "
print(espa)
reco = espa.strip()
print(reco)

# 31
print("")
print("Ejercicio 31")
print("Identificador del correcto")
ind = "30DaysOfPython"
ind2 = "thirty_days_of_python"
indCo = ind.isidentifier()
indCo1 = ind2.isidentifier()
print(indCo)
print(indCo1)
print("###############################################")
# Opcion más resumida de programar 
print(ind.isidentifier())
print(ind2.isidentifier())

# 32
print("")
print("Ejercicio 32")
unir = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# " .join(unir))

# 33