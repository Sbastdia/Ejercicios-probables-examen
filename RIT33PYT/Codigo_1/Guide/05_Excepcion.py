"""
Introducción a las excepciones
"""
import sys

# Primer número
numero1 = input("Introduzca un primer número: ")
try:
    numero1 = int(numero1)
except:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Segundo número
try:
    numero2 = int(input("Introduzca un segundo número: "))
except ValueError as e:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Hacer la comparación
comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)

