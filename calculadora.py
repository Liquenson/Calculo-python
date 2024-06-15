def calculadora_suma():
    while True:
        print("\nBienvenido a la calculadora de sumas.")
        print("1. Realizar una suma")
        print("2. Salir")

        opcion = input("Ingresa el número de la opción: ")

        if opcion == "2":
            print("¡Hasta luego!")
            break

        if opcion != "1":
            print("Opción no válida. Por favor, elige una opción válida.")
            continue

        try:
            cantidad_numeros = int(input("¿Cuántos números deseas sumar? "))
            if cantidad_numeros <= 0:
                print("Debes ingresar al menos un número.")
                continue

            numeros = []
            for i in range(cantidad_numeros):
                while True:
                    try:
                        num = float(input(f"Ingrese el número {i+1}: "))
                        numeros.append(num)
                        break
                    except ValueError:
                        print("Error: Debes ingresar un número válido.")

            resultado = sum(numeros)
            print("La suma es:", resultado)

        except ValueError:
            print("Error: Debes ingresar un número válido.")

        continuar = input("¿Deseas realizar otra suma? (s/n): ")
        if continuar.lower() != "s":
            print("¡Hasta luego!")
            break

# Llamar a la función para que se ejecute.
calculadora_suma()
