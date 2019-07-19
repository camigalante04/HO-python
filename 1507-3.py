def primo(num1):
    for x in range(1,num1):
        if num1%x==0 and x!=num1 and x!=1:   
            return False     #si es divisible por algun numero que no sea 1 y el mismo, no es primo
    return num1
#print(es_primo(3))   para verificar que funciona

def lista_primos(num2):         #creamos una lista con los primos menores al numero elegido
    for x in range(2,num2):
        if primo(x) != False:
            lista.append(x)
    return lista

#lista_primos(15)
#print(lista)

def divisible(lista,num3):
    for numero in lista:
        if num3%numero==0:
            factores.append(numero)
    return factores

def factores_x(numero):
    divisibles=[]
    while True:
        salida1=primo(numero)
        if salida1!=False:
            factores_finales.append(salida1)
            break
        else:
            lista_primos(numero)
            divisibles=divisible(lista,numero)
            factores_finales.append(divisibles[len(divisibles)-1])
            numero=numero//divisibles[len(divisibles)-1]
    factores_finales.reverse()
    return factores_finales

factores_finales=[]
lista=[]
factores=[]
print('Este programa calcula el mayor factor primo de un numero natural')
print('Ingrese un numero natural:')
numero=int(input())
print('El mayor factor primo de',numero,'es',max(factores_x(numero)))
