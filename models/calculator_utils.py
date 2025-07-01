from datetime import datetime
from classes.Consulta import Consulta


def sum(op1, op2):
    return op1 + op2


def rest(op1, op2):
    return op1 - op2


def mult(op1, op2):
    return op1 * op2


def div(op1, op2):
    try:
        resultado = op1 / op2
        return resultado
    except ZeroDivisionError:
        return "\033[31mNo se puede dividir por cero\033[0m"


def calculate(op1, operator, op2, usuario, consultas: Consulta):
    df = consultas.history
    result = None

    match operator:
        case '+':
            result = sum(op1, op2)
            print(f"Suma: {op1} {operator} {op2} = {result}")
        case '-':
            result = rest(op1, op2)
            print(f"Resta: {op1} {operator} {op2} = {result}")
        case '*':
            result = mult(op1, op2)
            print(f"Multiplicación: {op1} {operator} {op2} = {result}")
        case '/':
            result = div(op1, op2)
            if isinstance(result, str):
                print("\033[31mNo se puede dividir por cero\033[0m")
                return df
            else:
                print(f"División: {op1} {operator} {op2} = {result}")
        case _:
            print("\033[31mOperador no válido\033[0m")
            return df

    new_row = {
        'usuario': usuario,
        'operando1': op1,
        'operando2': op2,
        'operador': operator,
        'resultado': result,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    consultas.update_historial(new_row)
    return df
