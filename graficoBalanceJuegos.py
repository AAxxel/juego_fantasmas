import matplotlib.pyplot as plt


def calcular_porcentaje(numero, total):
    porcentaje = (numero / total) * 100
    return porcentaje

def graficar_victorias(p1,p2):

    labels = ['Ganadas', 'Perdidas']
    sizes = [calcular_porcentaje(p1,p1+p2), calcular_porcentaje(p2,p1+p2)]  
    colors = ['#ff9999','#66b3ff']  
    explode = (0.1, 0)  

    
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Estadísticas de victorias y derrotas')
    plt.axis('equal')  

    

def mostrar_grafico(p1,p2):
    graficar_victorias(p1,p2)
    plt.show()

def devolver_grafico(p1,p2):
    graficar_victorias(p1,p2)
    return plt.gcf()
