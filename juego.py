import random

# Base de preguntas por categoría
preguntas = {
    "Matemáticas": [
        {"pregunta": "¿Cuánto es 8 x 7?", "respuesta": "56", "pista": "Es mayor que 50"},
        {"pregunta": "¿Cuánto es 15 + 20?", "respuesta": "35", "pista": "Es menor que 40"},
    ],
    "Ciencias Naturales": [
        {"pregunta": "¿Qué planeta es conocido como el planeta rojo?", "respuesta": "marte", "pista": "Empieza con M"},
        {"pregunta": "¿Qué necesitan las plantas para hacer fotosíntesis?", "respuesta": "luz solar", "pista": "Proviene del Sol"},
    ],
    "Ciencias Sociales": [
        {"pregunta": "¿Cuál es el continente más grande?", "respuesta": "asia", "pista": "Empieza con A"},
        {"pregunta": "¿Qué país tiene forma de bota?", "respuesta": "italia", "pista": "Está en Europa"},
    ],
    "Cultura General": [
        {"pregunta": "¿Cuántos días tiene una semana?", "respuesta": "7", "pista": "Es más de 5"},
        {"pregunta": "¿Cuál es el idioma oficial de México?", "respuesta": "español", "pista": "Lo estás leyendo ahora"},
    ]
}

puntos = 0
nivel = 1

print("=" * 40)
print("      BIENVENIDO A MY PUZZLE")
print("=" * 40)

while True:
    print(f"\nNivel Actual: {nivel}")
    print(f"Puntos: {puntos}")

    # Menú de categorías
    categorias = list(preguntas.keys())

    print("\nSelecciona una categoría:")
    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")

    opcion = int(input("Opción: "))
    categoria = categorias[opcion - 1]

    reto = random.choice(preguntas[categoria])

    print("\n----- RETO -----")
    print(reto["pregunta"])

    intentos = 2
    correcto = False

    while intentos > 0:
        respuesta = input("Tu respuesta: ").lower().strip()

        if respuesta == reto["respuesta"]:
            correcto = True
            break
        else:
            intentos -= 1

            if intentos > 0:
                print("Respuesta incorrecta.")
                print("Pista:", reto["pista"])
                print("Te queda", intentos, "intento.")
            else:
                print("Fin del reto, sin puntos.")

    if correcto:
        ganados = nivel * 10
        puntos += ganados
        print(f"¡Correcto! Ganaste {ganados} puntos.")

        # Desbloqueo de niveles
        if puntos >= nivel * 20:
            nivel += 1
            print("¡Nuevo nivel desbloqueado!")

    print("\n¿Deseas seguir jugando?")
    print("1. Sí")
    print("2. No")

    continuar = input("Opción: ")

    if continuar != "1":
        break

print("\n========== FIN DEL JUEGO ==========")
print("Puntaje Final:", puntos)
print("Nivel Alcanzado:", nivel)
print("Gracias por jugar MY PUZZLE")