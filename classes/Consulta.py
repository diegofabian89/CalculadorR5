import pandas as pd

class Consulta:
    def __init__(self, df_history):
        self.history = df_history

    def update_historial(self, new_row):
        self.history = pd.concat([self.history, pd.DataFrame([new_row])], ignore_index=True)

    def all_operations(self):
        if self.history.empty:
            print("\033[31mNo hay operaciones registradas.\033[0m")
        else:
            print("\nOperaciones registradas:")
            print(self.history)

    def user_operations(self, user):
        df = self.history[self.history['usuario'] == user]
        if df.empty:
            print(f"\033[31mNo hay operaciones para el usuario: {user}\033[0m")
            return False
        else:
            print(f"\nOperaciones de {user}:")
            print(df)
            total = df['resultado'].sum()
            print(f"\nTotal de resultados: {total}")
            return True

    def operations_by_operator(self, operator):
        df = self.history[self.history['operador'] == operator]
        if df.empty:
            print(f"\033[31mNo hay operaciones con el operador: {operator}\033[0m")
        else:
            print(f"\nOperaciones con el operador {operator}:")
            print(df)

    def user_operations_by_operator(self, user, operator):
        df = self.history[
            (self.history['usuario'] == user) &
            (self.history['operador'] == operator)
        ]
        if df.empty:
            print(f"\033[31mNo hay operaciones para el usuario {user} con el operador {operator}\033[0m")
        else:
            print(f"\nOperaciones de {user} con el operador {operator}:")
            print(df)
            total = df['resultado'].sum()
            print(f"\nTotal de resultados filtrados: {total}")

    def delete_operation(self, user, indice):
        df_usuario = self.history[self.history['usuario'] == user]
        if indice not in df_usuario.index:
            print(f"\033[31mÍndice no válido para {user}.\033[0m")
            return False
        self.history = self.history.drop(indice).reset_index(drop=True)
        print(f"Operación en índice {indice} eliminada.")
        return True

