'''Se necesita elaborar un algoritmo en Python que solicite al usuario el número de respuestas correctas, 
incorrectas y en blanco correspondiente a los postulantes y muestre su puntaje final considerando que 
por cada respuesta correcta, tendrá 3 puntos, respuestas incorrectas tendrá -1 y respuestas en blanco será 0 (cero)'''

respuestasCorrectas = int(input("Ingrese el número de respuestas correctas: "))
respuestasIncorrectas = int(input("Ingrese el número de respuestas incorrectas: "))
respuestasBlanco = int(input("Ingrese el número de respuestas en blanco: "))

puntaje = (respuestasCorrectas*3) + (respuestasIncorrectas*-1) + (respuestasBlanco*0)

print(f"El puntaje final es: {puntaje}")