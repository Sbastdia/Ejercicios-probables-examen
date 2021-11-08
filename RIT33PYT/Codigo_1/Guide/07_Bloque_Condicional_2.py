"""
Introducción a los Bloques condicionales.

Un bloque condicional puede probar diferentes condiciones
"""
import sys


try:
    numero1 = int(input("Introduzca un primer número: "))
    numero2 = int(input("Introduzca un segundo número: "))
except ValueError as e:
    print("La conversión de al menos uno de los números no ha tenido éxito",
          file=sys.stderr)
    sys.exit()

# Hacer la comparación
if numero1 <= numero2:
    print(numero1, "<=", numero2)
elif numero1 >= numero2:
    print(numero1, ">=", numero2)
else:
    print(numero1, "==", numero2)

