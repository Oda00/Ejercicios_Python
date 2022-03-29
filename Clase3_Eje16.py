from random import randint
def ppt(op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    elif op==3:
        r="tijera"
    return r

ganadas=0

while ganadas<3:
    opUsario=int (input("Ingrese una opcion: \n1.-Piedra \n2._Papel \n3.-Tijera"))
    if opUsario>3 or opUsario<1:
        continue
    opMaquina=randint(1,3)
    print("La maquina elegio: ",ppt(opMaquina))
    print("El usario elegio: ",ppt(opUsario))
    if (opUsario==1 and opMaquina==3)or (opUsario==2 and opMaquina==1)or(opUsario==3 and opMaquina==2):
        print("Gana el usario")
        ganadas+=1
    elif opUsario==opMaquina:
            print("Es un empate")
    else:
            print("Gana la maquina")
    print("Ganadas: ", ganadas)

    
