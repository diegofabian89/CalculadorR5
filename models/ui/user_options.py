from models.validation_utils import isOperator
from models.validation_utils import isNumber


def view_user_operations(user, consultas):
    continuar = consultas.user_operations(user)
    if continuar:
        extra = input("\n¿Quieres ver tus operaciones filtradas por operador? (y/n): ").strip().lower()
        if extra == 'y':
            operator = input("Introduce el operador (+, -, *, /): ").strip()
            if isOperator(operator):
                consultas.user_operations_by_operator(user, operator)
            else:
                print("\n\033[31mOperador no válido.\033[0m")


def delete_option(user, consultas):
    df_usuario = consultas.history[consultas.history['usuario'] == user]
    if df_usuario.empty:
        print("\033[31mNo tienes operaciones para eliminar.\033[0m")
        return

    print("\nTu lista de operaciones\n")
    df_seleccion = df_usuario.loc[:, ['operador', 'fecha']]
    print("indice", df_seleccion)
    indice = input("\nIntroduce el indice: ").strip()
    if isNumber(indice):
        indice = int(indice)
        if not consultas.delete_operation(user, indice):
            print("\033[31mPrueba con indices de la lista.\033[0m")

        else:
            consultas.user_operations(user)
    else:
        print("\033[31mERROR introduce un valor numerio de la lista.\033[0m")
