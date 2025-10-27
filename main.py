import operaciones
from cuento import imprimir_cuento

def menu():
    print("\n=== PROYECTO COLABORATIVO PYTHON ===")
    print("1. Operaciones matemáticas")
    print("2. Imprimir un cuento")
    print("3. Salir")

while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- OPERACIONES MATEMÁTICAS ---")
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Suma: {operaciones.sumar(a, b)}")
            print(f"Resta: {operaciones.restar(a, b)}")
            print(f"Multiplicación: {operaciones.multiplicar(a, b)}")
            print(f"División: {operaciones.dividir(a, b)}")
            print(f"Potencia (base, potencia): {operaciones.potencias(a, b)}")
            print(f"Raíz (indice, radicando): {operaciones.raices(a, b)}")
        except ValueError:
            print("Por favor ingrese números válidos.")

    elif opcion == "2":
        print("\n--- CUENTOS DISPONIBLES ---")
        print("1. Dragón y montaña")
        print("2. Niña y bosque mágico")
        print("3. Ratón valiente")
        eleccion = input("Ingrese el número del cuento que desea leer: ")
        try:
            eleccion_num = int(eleccion)
            if eleccion_num in [1, 2, 3]:
                imprimir_cuento(eleccion_num)
            else:
                print("Opción no válida. Por favor seleccione 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número válido.")

    elif opcion == "3":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intente de nuevo.")
