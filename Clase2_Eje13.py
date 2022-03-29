frase=input("Ingrese la frase: ")
letra= input("Ingrese la letra: ")
cont=0

for carac in frase:
    if carac==letra:
        cont+=1
if cont>0:
    print("La letra "+letra+" se encontro "+ str(cont)+" veces")
else:
    print("No se encontro la letra "+letra)