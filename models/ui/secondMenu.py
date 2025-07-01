from models.validation_utils import isOperator, continuar
from models.ui.user_options import view_user_operations,delete_option


def queries_menu(user, consultas):
    while True:
        print("\nMenú de consultas:")
        print("1. Ver mis operaciones")
        print("2. Consultar todas la operaciones de todos los usuarios")
        print("3. Consultar operaciones de un usuario")
        print("4. Eliminar operación del historial")
        print("5. Volver al menu principal\n")

        opcion = input("Elige una opción: \n")

        match opcion:
            case '1':
                view_user_operations(user, consultas)

            case '2':

                consultas.all_operations()

                extra = input("\n¿Ver operaciones de este usuario por operator? (y/n): ")
                if continuar(extra):
                    operator = input("Introduce el operator (+, -, *, /): ")
                    if isOperator(operator):
                        consultas.operations_by_operator(operator)
                    else:
                        print("\033[31mOperador no válido.\033[0m")

            case '3':
                new_user = input("Introduce el usuario: ")
                view_user_operations(new_user, consultas)
            case '4':
                delete_option(user, consultas)
            case '5':
                print("\nVolviendo al menu principal ......")
                break
            case _:
                print("\033[31mOpción no válida.\033[0m")
