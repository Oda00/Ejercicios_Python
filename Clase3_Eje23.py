
A=[55,60,50,58,60,40,75,63]
suma=0
pesoMax=A[0]

for i in range (len(A)):
    for j in range (i+1,(len(A))):
        suma=A[i]+A[j]
        if suma<=150:
            print("La suma de: ", A[i],"+",A[j],"=",suma)
            if suma>pesoMax:
                pesoMax=suma
print ("El peso máximo posible es:",pesoMax)