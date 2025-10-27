import math 
# operaciones.py

def sumar(a, b):
    """Retorna la suma de dos números: a + b."""
    return a + b

def restar(a, b):
    """Retorna la resta de dos números: a - b."""
    return a - b

def multiplicar(a, b):
    """Retorna la multiplicacion de dos numeros: a * b."""
    return a * b  # Implementación de la multiplicación

def dividir(a, b):
    """Retorna la division de dos números: a / b. Maneja la división por cero."""
    if b == 0:
        return "Error: Division por cero no permitida."
    return a / b

def potencias(base, potencia):
    return math.pow(base, potencia)

def raices(indice, nummero):
    if indice == 2 and nummero < 0:
        return "Error: La raíz cuadrada de un número negativo no está definida."
    return math.pow(nummero, 1/indice)

# Bloque opcional para probar el módulo si se ejecuta directamente
if __name__ == "__main__":
    print("--- Pruebas de Modulo de Operaciones ---")
    print(f"Suma (10 + 5): {sumar(10, 5)}")
    print(f"Resta (10 - 5): {restar(10, 5)}")
    print(f"Multiplicacion (10 * 5): {multiplicar(10, 5)}")
    print(f"Division (10 / 5): {dividir(10, 5)}")
    print(f"Division por cero: {dividir(10, 0)}")
    print(f"Potencia de 3 elevado a 4: {potencias(3, 4)}")
    print(f"Raiz cuadrada de 25: {raices(2, 25)}")
    print(f"Raiz cuadrada de negativa: {raices(2, -1)}")
