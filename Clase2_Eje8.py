jornada=48
hTrabajada= int (input("Ingrese sus horas trabajadas:"))
pagoHora = 2
pagoExtra= 3.5


if hTrabajada <= jornada:
    salario=hTrabajada*pagoHora
else:
    salario=(jornada*pagoHora)+((hTrabajada-jornada)*pagoExtra)
print("Su pago total es de:", salario)