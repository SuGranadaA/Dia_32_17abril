#@Uso de *args y *kwargs


#Establecemos una función con fargs para sumar a+b sencilla y comparar
def sumar(a=1, b=2):
    return a + b


#Solicitamos los valores que vamos a utilizar en las funciones
val1 = (int(input("Ingrese por favor el valor 1: ")))
val2 = (int(input("Ingrese por favor el valor 2: ")))
val3 = (int(input("Ingrese por favor el valor 3: ")))
val4 = (int(input("Ingrese por favor el valor 4: ")))

#Imprimimos los valores ingresados por el usuario
print("\nEl valor 1 es: ", val1)
print("El valor 2 es: ", val2)
print("El valor 3 es: ", val3)
print("El valor 4 es: ", val4)

#Imprimimos el resultado de la suma predeterminada
print("\nEl resultado de la suma predeterminada es: ", sumar())

#Imprimimos el resultado de la suma con los valores ingresados
print("\nEl resultado de sumar ", val1, " y ", val2, " es: ",
      sumar(val1, val2))


#Definimos la fución para realizar una suma y dar su resultado en negativo
def sumanegativa(*args):
    res = 0
    #Establecemos que para cada arg en args se realice la siguiente operación
    for arg in args:
        res -= arg
    #Retornamos el valor modificado
    return res


#Imprimimos el resultado de la operación con los valores del usuario
print("\nEl resultado de sumar ", val1, " y ", val2, " en negativo es: ",
      sumanegativa(val1, val2))


#Definimos la función para sumar los equivalentes de un diccionario
def sumita(**kwargs):
    mass = 0
    #Establecemos que para cada key en kwargs se realice la operación
    for key in kwargs:
        mass += kwargs[key]
    #Retornamos el valor modificado
    return mass


#Imprimimos el resultado de la operación con los valores ingresados por el usuario
print("\nEl resultado de sumar ", val3, " y ", val4, " con *kwargs es: ",
      sumita(uno=val3, dos=val4))


#Definimos la función para sumar numeros, args y kwargs
def sumados(uno, dos=7, tres=14, *args, **kwargs):
    #Definimos el patrón de la operación
    mas = uno + dos + tres
    #Establecemos que para cada arg en args se realice la siguiente operación
    for val in args:
        mas += val
    #Establecemos que para cada key en kwargs se realice la operación
    for key in kwargs:
        mas += kwargs[key]
    return mas


#Imprimimos el resultado con los valores predeterminados
print("\nEl resultado de sumar 1 con los valores predeterminados es: ",
      sumados(1))

#Imprimimos el resultado con los valores ingresados por el usuario
print("\nEl resultado de sumar 1, ", val1, ", ", val2, ", ", val3, " y ", val4,
      " con *args y *kwargs es: ",
      sumados(1, val1, val2, cuatro=val3, cinco=val4))
