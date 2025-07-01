from models import data_utils, validation_utils
from models.ui import menu, welcome
from classes import Consulta


def main():
    df = data_utils.load_or_create_df()

    user = welcome.intro_user(df)

    consultas = Consulta.Consulta(df)

    menu.menu(user, consultas,df)

    consultas.history.to_csv('data/historial.csv', index=False)

    print("Historial guardado. ¡Hasta luego!")


if __name__ == "__main__":
    main()
