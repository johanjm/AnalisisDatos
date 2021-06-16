import numpy as np

def matrix():
    print("Multiplicación de matrices")
    print("Ingrese la dimensión de la primera matriz A de MxN")
    m1=int(input("Ingrese el valor de M: "))
    n1=int(input("Ingrese el valor de N: "))
    print("Ingrese la dimensión de la segunda matriz B de MxN")
    print("El valor de M es el valor de N de la primera matriz para que se pueda realizar la multiplicación")
    n2=int(input("Ingrese el valor de N: "))
    print("Ingrese los valor de la primera matriz")
    A=llenar(m1,n1)
    print("Ingrese los valor de la segunda matriz")
    B=llenar(n1,n2)
    print("La matriz A es:")
    print(A)
    print("La matriz B es:")
    print(B)
    C=multi(A,B,m1,n2,n1)
    print("La multiplicación es: ")
    print(C)

def llenar(x,y):
    matriz=np.zeros((x,y))
    for i in range (x):
        for j in range(y):
            print("Posisión (",i,",",j,"): ")
            matriz[i][j]=int(input("ingrese el valor: "))
    return matriz

def multi(a,b,x,y,z):
    matriz=np.zeros((x,y))
    for i in range (x):
        for j in range(y):
            aux=0
            for k in range(z):
                aux1=a[i][k]*b[k][j]
                aux=aux+aux1
            matriz[i][j]=aux
    return matriz

matrix()
