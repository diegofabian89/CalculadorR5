import os
import pandas as pd
import platform

path_file = 'data/historial.csv'
def load_or_create_df(path=path_file):
    if os.path.exists(path):
        df = pd.read_csv(path)
    else:
        datos = {
            'usuario': [],
            'operando1': [],
            'operando2': [],
            'operador': [],
            'resultado': [],
            'fecha': []
        }
        df = pd.DataFrame(datos)
        print("\033[31mArchivo no encontrado, creado DataFrame vacío.\033[0m")
    return df


def open_file(path):
    if platform.system() == 'Windows':
        os.startfile(path)