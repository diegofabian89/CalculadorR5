from models import data_utils
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import image as mpimg
import os


def generate_report(dframe):
    sns.set_style(style="whitegrid")

    df = pd.read_csv(dframe)

    if df.empty:
        print("\033[31mEl historial está vacío.\033[0m")
        exit()

    output_folder = os.path.join('reports')
    os.makedirs(output_folder, exist_ok=True)

    # Operaciones por usuario
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='usuario', palette='Set2')
    plt.title('Cantidad de operaciones por usuario')
    plt.ylabel('Número de operaciones')
    plt.xlabel('Usuario')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_folder}/operaciones_por_usuario.png')
    plt.close()

    #Gráfico 2: Operaciones por operador
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='operador', palette='Set1')
    plt.title('Cantidad de operaciones por operador')
    plt.xlabel('Operador')
    plt.ylabel('Frecuencia')
    plt.tight_layout()
    plt.savefig(f'{output_folder}/operaciones_por_operador.png')
    plt.close()

    #Gráfico 3: Suma total de resultados por usuario
    plt.figure(figsize=(8, 5))
    total_resultados = df.groupby('usuario')['resultado'].sum().reset_index()
    ax = sns.barplot(data=total_resultados, x='usuario', y='resultado', palette='coolwarm')
    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width() / 2,
            height + 1,
            f'{int(height)}',
            ha='center'
        )

    plt.title('Suma de resultados por usuario')
    plt.xlabel('Usuario')
    plt.ylabel('Resultado total')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_folder}/suma_resultados_por_usuario.png')
    plt.close()

    df['fecha'] = pd.to_datetime(df['fecha'])
    # Agrupar por día
    df['fecha_solo_dia'] = df['fecha'].dt.date
    operaciones_por_dia = df.groupby('fecha_solo_dia').size().reset_index(name='operaciones')

    # Graficar 4 operaciones por dia
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=operaciones_por_dia, x='fecha_solo_dia', y='operaciones', marker='o')
    plt.title('Cantidad de operaciones por día')
    plt.xlabel('Fecha')
    plt.ylabel('Nº de operaciones')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'{output_folder}/operaciones_por_dia.png')
    plt.close()

    #grafica 5 operaciones por hora
    df['hora'] = df['fecha'].dt.hour
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='hora', palette='magma')
    plt.title('Distribución de operaciones por hora')
    plt.xlabel('Hora del día')
    plt.ylabel('Número de operaciones')
    plt.tight_layout()
    plt.savefig(f'{output_folder}/operaciones_por_hora.png')
    plt.close()

    print("Reportes generados correctamente en la carpeta 'reportes'.")


    pdf_path = os.path.join(output_folder, 'reporte_calculadora.pdf')
    with PdfPages(pdf_path) as pdf:

        graficos = [
            'operaciones_por_usuario.png',
            'operaciones_por_operador.png',
            'suma_resultados_por_usuario.png',
            'operaciones_por_dia.png',
            'operaciones_por_hora.png'
        ]

        for grafico in graficos:
            ruta_img = os.path.join(output_folder, grafico)
            if os.path.exists(ruta_img):
                fig = plt.figure(figsize=(8, 6))
                img = mpimg.imread(ruta_img)
                plt.imshow(img)
                plt.axis('off')
                pdf.savefig(fig)
                plt.close(fig)

    print(f"PDF generado correctamente en: {pdf_path}")
    data_utils.open_file(pdf_path)

