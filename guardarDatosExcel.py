from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os
import matplotlib.pyplot as plt

def guardar_datos_y_graficos_en_excel(nombre_usuario, nombre, edad, numero_cuenta, grafico1, grafico2):
    
    wb = Workbook()
    ws = wb.active

    
    ws.append(['Nombre de usuario', 'Nombre', 'Edad', 'Numero de cuenta'])
    for cell in ws[1]:
        cell.font = cell.font.copy(bold=True)  
        cell.alignment = cell.alignment.copy(horizontal='center')  
    
    ws.append([nombre_usuario, nombre, edad, numero_cuenta])

   
    fig1 = plt.figure()
    grafico1.savefig(f'grafico_temporal_{nombre_usuario}_1.png')  
    plt.close(fig1)

    
    fig2 = plt.figure()
    grafico2.savefig(f'grafico_temporal_{nombre_usuario}_2.png')  
    plt.close(fig2)

   
    img_grafico1 = Image(f'grafico_temporal_{nombre_usuario}_1.png')  
    ws.add_image(img_grafico1, 'A5')  

    
    img_grafico2 = Image(f'grafico_temporal_{nombre_usuario}_2.png')  
    ws.add_image(img_grafico2, 'J5')  

    
    carpeta = 'excels'
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

   
    nombre_archivo = f'{nombre_usuario}_Datos.xlsx'  
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    wb.save(ruta_archivo)

   
    os.remove(f'grafico_temporal_{nombre_usuario}_1.png')
    os.remove(f'grafico_temporal_{nombre_usuario}_2.png')

    print(f'Los datos y los gráficos han sido guardados en el archivo "{ruta_archivo}".')
