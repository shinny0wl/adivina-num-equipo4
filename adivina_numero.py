import random
from datetime import datetime

GAME_TITLE = "Adivina el número"
DIFFICULTIES = {
    "1": {"name": "Fácil", "minimum": 1, "maximum": 20, "attempts": 8},
    "2": {"name": "Medio", "minimum": 1, "maximum": 50, "attempts": 7},
    "3": {"name": "Difícil", "minimum": 1, "maximum": 100, "attempts": 6},
}


def get_player_name():
    """Solicita y limpia el nombre del jugador, asignando uno por defecto si está vacío."""
    name = input("¿Cómo te llamas? ").strip()
    if not name:
        return "Jugador"
    return name


def choose_difficulty():
    """
    Muestra el menú de dificultades y repite la solicitud hasta que el usuario
    ingrese una opción válida (Mejora adicional).
    """
    print("\nSelecciona una dificultad:")
    for key, data in DIFFICULTIES.items():
        print(f"{key}. {data['name']} ({data['minimum']}–{data['maximum']}, {data['attempts']} intentos)")

    while True:
        choice = input("Opción: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Opción inválida. Por favor ingresa 1, 2 o 3.")


def read_guess(minimum, maximum):
    """
    Lee la entrada del usuario y garantiza que sea un entero dentro del rango permitido.
    No se penaliza al usuario si ingresa texto o números fuera de rango.
    """
    while True:
        raw_guess = input(f"Escribe un número entre {minimum} y {maximum}: ").strip()
        try:
            guess = int(raw_guess)
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            continue

        if guess < minimum or guess > maximum:
            print(f"El número debe estar entre {minimum} y {maximum}.")
            continue

        return guess


def calculate_score(attempts_used, maximum_attempts, won):
    """Calcula la puntuación obtenida en base a los intentos restantes."""
    if not won:
        return 0

    points = (maximum_attempts - attempts_used + 1) * 10
    return max(points, 10)


def play_round(difficulty_config):
    """Ejecuta una ronda respetando estrictamente el número máximo de intentos."""
    minimum = difficulty_config["minimum"]
    maximum = difficulty_config["maximum"]
    max_attempts = difficulty_config["attempts"]

    secret_number = random.randint(minimum, maximum)
    attempts_used = 0
    won = False

    print(f"\nAdivina el número entre {minimum} y {maximum}. Tienes {max_attempts} intentos.")

    while attempts_used < max_attempts and not won:
        guess = read_guess(minimum, maximum)
        attempts_used += 1

        if guess < secret_number:
            print(f"Muy bajo. (Te quedan {max_attempts - attempts_used} intentos)")
        elif guess > secret_number:
            print(f"Muy alto. (Te quedan {max_attempts - attempts_used} intentos)")
        else:
            print("¡Correcto!")
            won = True

    if won:
        print(f"¡Felicidades! Adivinaste en {attempts_used} intento(s).")
    else:
        print(f"Se acabaron los intentos. El número secreto era {secret_number}.")

    score = calculate_score(attempts_used, max_attempts, won)
    return {
        "won": won,
        "attempts": attempts_used,
        "score": score,
        "secret_number": secret_number,
    }


def save_score(scores, player_name, result, difficulty_name):
    """Registra y ordena los puntajes obtenidos."""
    record = {
        "name": player_name,
        "score": result["score"],
        "won": result["won"],
        "difficulty": difficulty_name,
        "played_at": datetime.now(),
    }
    scores.append(record)
    scores.sort(key=lambda item: item["score"], reverse=True)
    return record


def show_leaderboard(scores):
    """Muestra los mejores puntajes de la sesión actual."""
    print("\n--- Mejores resultados de esta sesión ---")
    if not scores:
        print("Todavía no hay resultados.")
        return

    for position, result in enumerate(scores[:3], start=1):
        print(
            f"{position}. {result['name']} — {result['score']} puntos "
            f"({result['difficulty']})"
        )


def play_game(scores):
    """Coordina el flujo completo de una partida."""
    player_name = get_player_name()
    difficulty_config = choose_difficulty()
    result = play_round(difficulty_config)
    save_score(scores, player_name, result, difficulty_config["name"])
    show_leaderboard(scores)


def ask_to_play_again():
    """
    Pregunta si se desea jugar otra vez tolerando espacios, mayúsculas y variantes comunes.
    """
    valid_yes = {"s", "si", "sí", "y", "yes"}
    valid_no = {"n", "no"}

    while True:
        answer = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if answer in valid_yes:
            return True
        if answer in valid_no:
            return False
        print("Respuesta no válida. Por favor escribe 's' para sí o 'n' para no.")


def main():
    print(f"=== {GAME_TITLE} ===")
    print("Adivina el número secreto y consigue la mayor puntuación.")
    scores = []

    while True:
        play_game(scores)
        if not ask_to_play_again():
            break

    print("\nGracias por jugar.")


if __name__ == "__main__":
    main()