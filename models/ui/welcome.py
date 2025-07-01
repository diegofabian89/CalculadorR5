from models import validation_utils


def intro_user(df):
    user = ""
    while not user.strip():
        user = input("Hola, introduce tu nombre: ").strip()
        if not user:
            print("Por favor, introduce un nombre válido.")

    if validation_utils.userExists(user, df):
        print(f"¡Bienvenido de nuevo, {user.upper()}!")
    else:
        print(f"Hola {user.upper()}, parece que eres nuevo por aquí. ¡Bienvenido!")

    return user