''''import datetime as data
fecha_llegada = data.datetime.now()
print(f"La fecha y la hora de llegada: {fecha_llegada}")
print(fecha_llegada.strftime("%Y-%m-%d"))
f1=data.date(2025,10,5)
f2=data.date(2025,10,25)
print(f"Total de dias: {f2-f1}")
diferencia= f1-f2
print(f"Total de dias: {diferencia.days}")'''

#Registrar fecha de nacimiento y decir cuantos anos tengo
import datetime as data
import dateutil.relativedelta as rela 
#python -m pip install python-dateutil           
'''
f1=data.date(1999,12,17)
f2=data.date(2025,10,7)

diferencia= rela.relativedelta(f2,f1)
print(f"Anos: {diferencia.years}")
print(f"Meses: {diferencia.months}")
print(f"Dias: {diferencia.days}")
'''

def fechauser():
    while True:
        try:
            anio = int(input("Ingrese año de nacimiento: "))
            if anio < 1900 or anio > 2025:
                print("Año inválido. Debe estar entre 1900 y 2025.")
                continue

            mes = int(input("Ingrese número del mes de nacimiento: "))
            if mes < 1 or mes > 12:
                print("Mes inválido. Debe estar entre 1 y 12.")
                continue

            dia = int(input("Ingrese día de nacimiento: "))
            fecha_nac = data.date(anio, mes, dia)
            return fecha_nac

        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar solo números válidos para una fecha real.")

#Pedimos fecha de nacimiento al usuario
fecha_nacimiento = fechauser()

# Fecha actual
fecha_actual = data.date(2025, 10, 7)

# Calcular diferencia
diferencia = rela.relativedelta(fecha_actual, fecha_nacimiento)

print(f"Años: {diferencia.years}")
print(f"Meses: {diferencia.months}")
print(f"Días: {diferencia.days}")



'''
fecha_nacimiento=input("Ingrese fecha de nacimiento: ")
fecha_actual= data.datetime.now()
anos_edad= fecha_nacimiento-fecha_actual
print(f"Total de anos: {anos_edad.years}") '''