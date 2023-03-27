#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#respuesta: 5 porque es el valor que retorna la función

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#respuesta: "number_of_days_in_a_week_silicon_or_triangle_sides" es una cadena de caracteres y no una función y no esta definida en la función.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#respuesta: es 5 debido a que se toma siempre el primer return. 

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#respuesta: te imprime 5 debido al return que le da valor 5 a "number_of_fingers".

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# la respuesta es 5 porque esta imprimiendo el number_of_great_lakes que se remplazo por el x 



#6 
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# la respuesta de esta funcion es 3 y 5 ya que add(1,2) y add(2,3) se tienen que sumar y declara el resultado de cada una 


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# la respuesta de esta funcion es 25 ya que me esta pdiendo sumar b + c pero al ser str se juntan y me da de resultado 25


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# la respuesta es 10 por que b no es menor que 10 es mas grande ya que es 100 entonces imprime el else 

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#la salida de la funcion es 7 + 14 y en la ultima llamada seria 21 

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# aqui la respuesta es 8 ya que me esta retornando a b+c lo cual b seria 3 y c seria 5 y esos dos al sumarse daria 8 


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

# la salida sera 500 luego 500 luego llama a la funcion que me muestra 300 y luego me va a mostar 500 


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# la salida sera 500 luego 500 luego llama a la funcion que me muestra 300 y luego me va a mostar 500 


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# la salida sera 500 luego 500 llamara a la funcion que muestra 300 y luego 300 nuevamente 


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# la saida es 1 , 2 y la ultima es 3 ya que se estan imprimiendo por separado las funciones  


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#la salida de la primera funcion es 1 y 3 y la salida de la 2da funcion es 5 y 10