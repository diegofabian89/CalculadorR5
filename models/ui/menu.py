from models.validation_utils import isNumber, isOperator
from models.calculator_utils import calculate
from models.ui.secondMenu import queries_menu
from models.report import generate_report


def number_request(text):
    value = input(text)
    if not isNumber(value):
        print("\033[31mERROR: no es un número.\033[0m")
        return None
    return float(value)


def operator_request():
    operator = input("Introduce el operador (+ , - , * , / ) ")
    if not isOperator(operator):
        print("\033[31mERROR: operador no válido.\033[0m")
        return None
    return operator


def menu(user, consultas, dframe):
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Calcular")
        print("2. Consultar historial operaciones")
        print("3. Iniciar sesión con otro usuario")
        print("4. Generar reporte y visualizar")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                op1 = number_request("Introduce Operando uno: ")
                if op1 is None:
                    continue

                operator = operator_request()
                if operator is None:
                    continue

                op2 = number_request("Introduce Operando dos: ")
                if op2 is None:
                    continue

                calculate(op1, operator, op2, user, consultas)

            case "2":
                queries_menu(user, consultas)

            case "3":
                print("\nGuardando historial y cambiando de usuario...\n")
                consultas.history.to_csv('data/historial.csv', index=False)
                from main import main
                main()
                return
            case "4":
                consultas.history.to_csv('data/historial.csv', index=False)
                generate_report("data/historial.csv")

            case "5":
                print("Saliendo de la calculadora...")
                break
            case _:
                print("\033[31mOpción no válida. Intenta de nuevo.\033[0m")
