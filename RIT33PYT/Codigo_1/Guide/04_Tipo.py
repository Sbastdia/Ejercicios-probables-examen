"""
Conversión a un entero y comparación

(probar con un dato introducido que no es un número)
"""

# Primer número
numero1 = input("Introduzca un primer número: ")
numero1 = int(numero1)

# Segundo número
numero2 = int(input("Introduzca un segundo número: "))

# Hacer la comparación
comparacion = numero1 < numero2

print(numero1, "<", numero2, ":", comparacion)

