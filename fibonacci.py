#Escribir un programa de python para hacer la serie de Fibonacci entre 0 y 50, la serie de Fibonacci es: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

listFibonacci = [0, 1]

while len(listFibonacci)<50:
    lengthOfList = len(listFibonacci)
    listFibonacci.append(listFibonacci[lengthOfList-1] + listFibonacci[lengthOfList-2])

print(listFibonacci)