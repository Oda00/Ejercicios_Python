correctos= int (input("Ingrese el número de aciertos "))
errores= int (input("Ingrese el número de errores "))
total= correctos+errores
pco=(100/total)*correctos
pin=(100/total)*errores
print("Su puntaje final es: "+str(correctos)+ "/" +str(total))
print("Su porcentaje de aciertos es: %.2f y un porcentaje de errores de: %.2f" %(pco,pin) )