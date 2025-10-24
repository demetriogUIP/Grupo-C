import operaciones

# ... (import cuento si ya está)

print("--- Proyecto Colaborativo Python ---")
print("Calculos:")

# Uso directo de las funciones de operaciones.py
num1 = 20
num2 = 8
num_cero = 0

resultado_suma = operaciones.sumar(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado_suma}")

resultado_resta = operaciones.restar(num1, num2)
print(f"La resta de {num1} y {num2} es: {resultado_resta}")

# Nuevas funciones
resultado_multiplicacion = operaciones.multiplicar(num1, num2)
print(f"La multiplicacion de {num1} y {num2} es: {resultado_multiplicacion}")

resultado_division = operaciones.dividir(num1, num2)
print(f"La division de {num1} y {num2} es: {resultado_division}")

resultado_division_cero = operaciones.dividir(num1, num_cero)
print(f"Division por cero ({num1} y {num_cero}): {resultado_division_cero}")


# ... (Espacio para el Colaborador de 'cuento.py')