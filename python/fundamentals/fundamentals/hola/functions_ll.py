def lista(num):
    lista = []
    for x in range(num,-1,-1):
        lista.append(x)
    return lista

print(lista(5))



def imprimir_y_devolver ():
    b = 1
    print(b)
    if b < 0:
        return 5
    else:
        return 2
    return 7
print(imprimir_y_devolver ())



def lista_mas_su(num ):
    lista = []
    for x in range(num ,0,-1):
        lista.append(x)

    print(min(lista) + max(lista))
    return lista

print(lista_mas_su(5))


def lista_valor_largo(lista):
    if len(lista) < 2:
        return False
    output = []
    for i in range (0 , len (lista )):
        if lista [i] > lista [ 1 ]:
            output.append(lista[i])
    print(len(output))
    return output
print( lista_valor_largo([5 , 2 ,3 ,2 ,1 , 4]))
print(lista_valor_largo([3]))


def longitud_ese_valor( valor , tamaño):
    output = []
    for i in range ( 0 , tamaño):
        output.append ( valor )
    return output
print(longitud_ese_valor(7 , 4)) 
print(longitud_ese_valor(2 , 6))