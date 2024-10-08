
import random
import math
from crearUser import crear_usuario
from graficoMejoresJugadores import mostrar_grafico_puntaje, devolver_grafico_puntaje
from graficoBalanceJuegos import mostrar_grafico, devolver_grafico
from guardarDatosExcel import guardar_datos_y_graficos_en_excel
from eliminarUser import eliminar_usuario

menu_principal = True
menu_sesion = None
opcion_menu_principal = ''
opcion_menu_sesion = ''
tablero = ''
usuario_creado = False

llaveConfig, respuesta, buenoLimite, maloLimite, iterador, iterador2, llaveConfig2 = 1, 0, 0, 0, 0, 0, 1

cantidad_usuarios_creados = 0
cantidad_usuarios = 50
numeros_cuentas = []
nombres_completos = []
edades = []
usernames = []
passwords = []
puntos = [] 
totalVictorias = []
totalDerrotas = []
partidas = {}
tablero = [[None] * 8 for _ in range(8)]
Fantasmas_buenos1 = [[None] * 4 for _ in range(5)]
Fantasmas_malos1 = [[None] * 4 for _ in range(5)]
Fantasmas_buenos2 = [[None] * 4 for _ in range(5)]
Fantasmas_malos2 = [[None] * 4 for _ in range(5)]

nuevo_num_cuenta, nuevo_nombre_completo, nuevo_username, invitado, local, partidas = "", "", "", "", "", ""
nuevo_edad, llave, llave2, x, i, opcion_mover, totalFantasmas, totalFantasma, auxFantasma = 0, 0, 0, 0, 0, 0, 0, 0, 0
jugador = 1
nuevo_puntos = 0.0
jugador_gana = False


username_login, password_login, ganador, perdedor, temp_n = "", "", "", "", 0


partidas = []
edades = []
usernames = []
passwords = []
nombres_completos = []
numeros_cuentas = []
puntos = []
totalDerrotas = []
totalVictorias = []

def reiniciarFantasmas():
    global Fantasmas_buenos1
    global Fantasmas_malos1
    global Fantasmas_buenos2
    global Fantasmas_malos2

    Fantasmas_buenos1 = [[0] * 4 for _ in range(5)]
    Fantasmas_malos1 = [[0] * 4 for _ in range(5)]
    Fantasmas_buenos2 = [[0] * 4 for _ in range(5)]
    Fantasmas_malos2 = [[0] * 4 for _ in range(5)]

def organizarFantasmas1(tamanio, tamX, tamY):


    Fantasmas_cual = [[None] * 4 for _ in range(tamanio)]
    global Fantasmas_buenos1
    
    global Fantasmas_malos1

    Fantasmas_buenos1 = [[0] * 4 for _ in range(5)]
    Fantasmas_malos1 = [[0] * 4 for _ in range(5)]

    mitad_redondeada = math.floor(tamanio / 2)
    e = 1
    while e < tamanio:  
        x1 = random.randrange(tamX, 7)
        y1 = random.randrange(6, tamY)
        
        
        fantasmaExiste = False
        for i in range(1, e):
            if Fantasmas_cual[i][1] == x1 and Fantasmas_cual[i][2] == y1:
                fantasmaExiste = True
                break
        
        
        if not fantasmaExiste:
            Fantasmas_cual[e][1] = x1
            Fantasmas_cual[e][2] = y1
            e += 1  

    
    for e in range(1, mitad_redondeada+1): 
        Fantasmas_buenos1[e][1] = Fantasmas_cual[e][1]
        Fantasmas_buenos1[e][2] = Fantasmas_cual[e][2]
        Fantasmas_buenos1[e][0] = 1
       

    for e in range(1, mitad_redondeada+1):  
        Fantasmas_malos1[e][1] = Fantasmas_cual[e+mitad_redondeada][1]
        Fantasmas_malos1[e][2] = Fantasmas_cual[e+mitad_redondeada][2]
        Fantasmas_malos1[e][0] = 1
        

def organizarFantasmas2(tamanio, tamX, tamY):
    Fantasmas_cual = [[None] * 4 for _ in range(tamanio)]
    e = 1
    global Fantasmas_buenos2
    
    global Fantasmas_malos2
    Fantasmas_buenos2 = [[0] * 4 for _ in range(5)]
    Fantasmas_malos2 = [[0] * 4 for _ in range(5)]
    mitad_redondeada = math.floor(tamanio / 2)
    while e < tamanio:  
        x1 = random.randrange(tamX, 7)
        y1 = random.randrange(2, tamY)
        
        
        fantasmaExiste = False
        for i in range(1, e):
            if Fantasmas_cual[i][1] == x1 and Fantasmas_cual[i][2] == y1:
                fantasmaExiste = True
                break
        
        
        if not fantasmaExiste:
            Fantasmas_cual[e][1] = x1
            Fantasmas_cual[e][2] = y1
            e += 1  

    
    for e in range(1, mitad_redondeada+1): 
        Fantasmas_buenos2[e][1] = Fantasmas_cual[e][1]
        Fantasmas_buenos2[e][2] = Fantasmas_cual[e][2]
        Fantasmas_buenos2[e][0] = 1
        

    for e in range(1, mitad_redondeada+1):  
        Fantasmas_malos2[e][1] = Fantasmas_cual[e+mitad_redondeada][1]
        Fantasmas_malos2[e][2] = Fantasmas_cual[e+mitad_redondeada][2]
        Fantasmas_malos2[e][0] = 1

def verificarMovimientos(mox, moy, cordFamx, cordFamy):
    if mox == cordFamx and moy == cordFamy-1:
        return "1"
    elif mox == cordFamx and moy == cordFamy+1:
        return "2"
    elif mox == cordFamx-1 and moy == cordFamy:
        return "3"
    elif mox == cordFamx+1 and moy == cordFamy:
        return "4"
    else:
        return "5"

def verificarSiJuegoExiste(user):
    global totalDerrotas
    global totalVictorias
    global cantidad_usuarios_creados
    global usernames
    for i in range(cantidad_usuarios_creados):
        if usernames[i] == user:
            if totalDerrotas[i] == 0 and totalVictorias[i] == 0:
                return True
    return False

def crearTablero():
    global tablero
    reiniciarFantasmas()
    for posFila in range(1, 8):
        for posColumna in range(1, 8):
            if posColumna == 1 and posFila == 1:
                tablero[posFila][posColumna] = "   "
            elif posFila == 1:
                tablero[posFila][posColumna] = " " + str(posColumna - 1) + " "
            elif posColumna == 1:
                tablero[posFila][posColumna] = " " + str(posFila - 1) + " "
            else:
                tablero[posFila][posColumna] = " _ "


def manual(large, jugador, array_fantasma, valor, turno, tipoFantasma):
    global tablero
    corX, corY = 0,0
    print("Jugador "+ jugador)
    for i in range(1,large):
        cordenadas_validas = False
        while not cordenadas_validas:
            print("Ingrese las cordenadas en X donde quiere su Fantasma "+ tipoFantasma + " #" + str(i))
            corX = int(input()) +1
            print("Ingrese las cordenadas en Y donde quiere su Fantasma "+ tipoFantasma + " #" + str(i))
            corY = int(input()) +1
            if (corX < 8 and corY < 8) and (corX > 1 and corY > 1):
                if (turno == 2 and (corY == 2 or corY == 3 or corY == 4)) or (turno == 1 and (corY == 5 or corY == 6 or corY == 7)):
                    if tablero[corY][corX] == " _ ":
                        tablero[corY][corX] = valor
                        array_fantasma[i][1] = corX
                        array_fantasma[i][2] = corY
                        array_fantasma[i][0] = 1
                        cordenadas_validas = True
                    else:
                        print("Ese espacio ya se esta ocupando")
                else:
                    print("No invadas espacio ajeno")

            else:
                print("Cordenada incorrecta")

while menu_principal == True:
    logged_in = False
    print("")
    print("*** MENÚ DE INICIO ***")
    print("1 -> Login")
    print("2 -> Crear Player")
    print("3 -> Salir")
    opcion_menu_principal = int(input("Opción: "))


    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    if opcion_menu_principal == 1:
        print("")
        print("*** LOGIN ***")
        username_login = input("Username: ")
        password_login = input("Password: ")
        
        local = username_login
        
        pos = 0
        while pos < cantidad_usuarios_creados:
            if pos < len(usernames) and pos < len(passwords):
                if usernames[pos] == username_login and passwords[pos] == password_login:
                    local = username_login
                    logged_in = True
            pos += 1

        if logged_in:
            print("¡Ha iniciado sesión!")
            menu_sesion = True 
            while menu_sesion == True:
                print("")
                print("*** MENÚ PRINCIPAL ***")
                print("1 -> Jugar GHOSTS")
                print("2 -> Configuración")
                print("3 -> Reportes")
                print("4 -> Mi perfil")
                print("5 -> Cerrar sesión")
                opcion_menu_sesion = int(input("Opción: "))

                if opcion_menu_sesion == 1:
                    jugador_gana = False
                    
                    import os
                    os.system('cls' if os.name == 'nt' else 'clear')

                    invitado = ""
                    pos = 1

                    print("")
                    print("*** Usuario jugador invitado ***")
                    username_login = input("Username: ")

                    pos = 0
                    while pos < cantidad_usuarios_creados:
                        if pos < len(usernames):
                            if usernames[pos] == username_login and username_login != local:
                                invitado = username_login
                        pos += 1


                    if invitado == "":
                        print("Usuario no encontrado o iniciado")
                        llave = 1
                    else:
                        llave = 0
                        
                        crearTablero()
                   
                    if llaveConfig == 1:
                        
                        tablero[2][3] = "F2 "
                        tablero[2][4] = "F2 "
                        tablero[2][5] = "F2 "
                        tablero[2][6] = "F2 "
                        tablero[3][4] = "F2 "
                        tablero[3][5] = "F2 "
                        tablero[3][6] = "F2 "
                        tablero[3][3] = "F2 "
                        # Jugador 1
                        tablero[6][3] = "F1 "
                        tablero[6][4] = "F1 "
                        tablero[6][5] = "F1 "
                        tablero[6][6] = "F1 "
                        tablero[7][4] = "F1 "
                        tablero[7][5] = "F1 "
                        tablero[7][6] = "F1 "
                        tablero[7][3] = "F1 "
                        if llaveConfig2 == 1:

                            organizarFantasmas1(9,3,8)
                            organizarFantasmas2(9,3,4)


                        elif llaveConfig2 == 2:

                            crearTablero()
                            #Jugador 1
                            manual(5, local, Fantasmas_buenos1, "F1 ",1, "bueno")
                            manual(5, local, Fantasmas_malos1, "F1 ",1,"malo")
                            

                            #Jugador 2
                            manual(5, invitado, Fantasmas_buenos2, "F2 ",2, "bueno")
                            manual(5, invitado, Fantasmas_malos2, "F2 ",2 , "malo")

                            

                        fantasmaBuenoTotal1 = 4
                        fantasmaBuenoTotal2 = 4
                        fantasmaMaloTotal1 = 4
                        fantasmaMaloTotal2 = 4

                    elif llaveConfig == 2:
                        # Configuración de los fantasmas en el tablero
                        tablero[2][5] = "F2 "
                        tablero[2][6] = "F2 "
                        tablero[3][5] = "F2 "
                        tablero[3][6] = "F2 "

                        # Jugador 1
                        tablero[6][5] = "F1 "
                        tablero[6][6] = "F1 "
                        tablero[7][5] = "F1 "
                        tablero[7][6] = "F1 "
                        if llaveConfig2 == 1:
                            # Fantasmas buenos del jugador 1 en X
                            
                            organizarFantasmas1(5,5,8)
                            organizarFantasmas2(5,5,4)
                            
                           

                        elif llaveConfig2 == 2:    
                            crearTablero()
                            #Jugador 1
                            manual(3, local, Fantasmas_buenos1, "F1 ",1, "bueno")
                            manual(3, local, Fantasmas_malos1, "F1 ",1,"malo")
                            

                            #Jugador 2
                            manual(3, invitado, Fantasmas_buenos2, "F2 ",2, "bueno")
                            manual(3, invitado, Fantasmas_malos2, "F2 ",2 , "malo")

                        fantasmaBuenoTotal1 = 2
                        fantasmaBuenoTotal2 = 2
                        fantasmaMaloTotal1 = 2
                        fantasmaMaloTotal2 = 2
            
                        

                    elif llaveConfig == 3:
                        tablero[2][6] ="F2 "
                        tablero[3][6]="F2 "

                        # Jugador 1

                        tablero[6][6]="F1 "
                        tablero[7][6]="F1 "

                        if llaveConfig2 == 1:

                            organizarFantasmas1(3,6,8)
                            organizarFantasmas2(3,6,4)


                        elif llaveConfig2 == 2:
                            crearTablero()
                            #Jugador 1
                            manual(2, local, Fantasmas_buenos1, "F1 ",1, "bueno")
                            manual(2, local, Fantasmas_malos1, "F1 ",1,"malo")
                            

                            #Jugador 2
                            manual(2, invitado, Fantasmas_buenos2, "F2 ",2, "bueno")
                            manual(2, invitado, Fantasmas_malos2, "F2 ",2 , "malo")

                        fantasmaBuenoTotal1 = 1
                        fantasmaBuenoTotal2 = 1
                        fantasmaMaloTotal1 = 1
                        fantasmaMaloTotal2 = 1
                    
                    else:
                        print("Opcion invalida")
                    
                    pos = 1

                    while llave == 0:
                        print("Jugador " + local + ":")
                        print("Fantasmas Buenos: " + str(fantasmaBuenoTotal1))
                        print("Fantasmas Malos: " + str(fantasmaMaloTotal1))
                        print("")
                        print("Jugador " + invitado)
                        print("Fantasmas Buenos: " + str(fantasmaBuenoTotal2))
                        print("Fantasmas Malos: " + str(fantasmaMaloTotal2))

                        if jugador == 1:
                            print("Turno del jugador: " + local)
                        else:
                            print("Turno del jugador: " + invitado)

                        for posFila in range(1, 8):
                            for posColumna in range(1, 8):
                                print(tablero[posFila][posColumna], end=" ")
                            print("")

                        x = -1
                        i = -1
                        llave2 = 0

                        while True:
                            print("Seleccione una coordenada Y entre 1 y 6")
                            x = int(input())

                            print("Seleccione una coordenada X entre 1 y 6")
                            i = int(input())
                            
                            if 0 < x < 7 and 0 < i < 7:
                                if tablero[x + 1][i + 1] == " " + "_" + " ":
                                    print("Lugar vacío")
                                    x = -2
                                    i = -2
                                else:
                                    if jugador == 1:
                                        if tablero[x + 1][i + 1] == "F2" + " ":
                                            print("Pieza ajena")
                                            x = -2
                                            i = -2
                                    else:
                                        if tablero[x + 1][i + 1] == "F1" + " ":
                                            print("Pieza ajena")
                                            x = -2
                                            i = -2
                            else:
                                print("Valor inválido")
                                
                            if x == -1 or i == -1:
                                break
                            
                            elif x < 0 or x > 7 or i < 0 or i > 7:
                                print("Escriba coordenadas correctas")
                                
                            else:
                                print("Lugar seleccionado")
                                break

                               

                        if x == -1 or i == -1:
                            print("Seguro que quieres salir?")
                            print("1. SI")
                            print("2. NO")
                            respuesta = input("Ingrese su respuesta: ")

                            if respuesta == "1":
                                if jugador == 1:
                                    print("===========¡FELICIDADES! Ganador: JUGADOR " + invitado +  "============ ")
                                    ganador = invitado
                                    perdedor = local
                                else:
                                    print("===========¡FELICIDADES! Ganador: JUGADOR " + local +  "============ ")
                                    ganador = local
                                    perdedor = invitado
                                llave = 1
                        
                        else:
                            
                            i = i + 1
                            x = x +1
                          
                            while True:

                                print("Seleccione hacia qué lugar se quiere mover en X:")
                                xMover = int(input())
                                print("Seleccione hacia qué lugar se quiere mover en Y:")
                                yMover = int(input())

                                opcion_mover = verificarMovimientos(xMover, yMover, i-1, x-1)
                                if jugador == 1:
                                    if opcion_mover == "1":
                                        if (x == 2 and i == 7) or (x == 2 and i == 2):
                                            for iterador in range(1, 5):
                                                if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x:
                                                    llave = 1
                                                    llave2 = 1
                                                    print("===========¡FELICIDADES! Ganador: JUGADOR " + local +  "============ ")
                                                    ganador = local
                                                    perdedor = invitado
                                                    jugador_gana = True
                                                    break
                                            if jugador_gana == True:
                                                break

                                        if x == 2:
                                            print("No te puedes mover hacia arriba")
                                        else:
                                            if tablero[x][i] == tablero[x-1][i]:
                                                print("¡Fuego amigo!")
                                            else:
                                                if tablero[x-1][i] == "F2 ":
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x-1:
                                                            Fantasmas_buenos2[iterador][0] = 0
                                                            Fantasmas_buenos2[iterador][1] = 0
                                                            Fantasmas_buenos2[iterador][2] = 0
                                                            print("Has ahuyentado un fantasma bueno de " + invitado)
                                                        if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x-1:
                                                            Fantasmas_malos2[iterador][1] = 0
                                                            Fantasmas_malos2[iterador][2] = 0
                                                            Fantasmas_malos2[iterador][0] = 0
                                                            print("Has ahuyentado un fantasma malo de " + invitado)
                                                print("Te moviste hacia arriba")
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x:
                                                        Fantasmas_buenos1[iterador][1] = i
                                                        Fantasmas_buenos1[iterador][2] = x-1
                                                      #  print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                        
                                                    if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x:
                                                        Fantasmas_malos1[iterador][1] = i
                                                        Fantasmas_malos1[iterador][2] = x-1
                                                      #  print("Fantasma en x: "+ str(Fantasmas_malos1[iterador][1]) + " en y:" + str(Fantasmas_malos1[iterador][2]))
                                                        
                                                tablero[x-1][i] = "F1 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break
                                        
                                    
                                        

                                    elif opcion_mover == "2":
                                        
                                        if x == 7:
                                            print("No te puedes mover hacia abajo")
                                        else:
                                            if tablero[x+1][i] == tablero[x][i]:
                                                print("¡Fuego amigo!")
                                            else:
                                                if tablero[x+1][i] == "F2 ":
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x+1:
                                                            Fantasmas_buenos2[iterador][0] = 0
                                                            Fantasmas_buenos2[iterador][1] = 0
                                                            Fantasmas_buenos2[iterador][2] = 0
                                                            print("Has ahuyentado un fantasma bueno de " + invitado)
                                                        if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x+1:
                                                            Fantasmas_malos2[iterador][1] = 0
                                                            Fantasmas_malos2[iterador][2] = 0
                                                            Fantasmas_malos2[iterador][0] = 0
                                                            print("Has ahuyentado un fantasma malo de " + invitado)
                                                print("Te moviste hacia abajo")
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x:
                                                       # print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                        Fantasmas_buenos1[iterador][1] = i
                                                        Fantasmas_buenos1[iterador][2] = x+1
                                                      #  print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                    if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x:
                                                        Fantasmas_malos1[iterador][1] = i
                                                        Fantasmas_malos1[iterador][2] = x+1
                                                tablero[x+1][i] = "F1 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break


                                    elif opcion_mover == "3":
                                        if i == 2:
                                            print('No te puedes mover hacia la izquierda')
                                        else:
                                            if tablero[x][i-1] == tablero[x][i]:
                                                print('Fuego amigo!')
                                            else:
                                                
                                                if tablero[x][i-1] == "F2 ":
                                                    
                                                    for iterador in range(1, 5):
                                                        
                                                        if Fantasmas_buenos2[iterador][1] == i-1 and Fantasmas_buenos2[iterador][2] == x:
                                                            
                                                            Fantasmas_buenos2[iterador][0] = 0
                                                            Fantasmas_buenos2[iterador][1] = 0
                                                            Fantasmas_buenos2[iterador][2] = 0
                                                            print('Has ahuyentado un fantasma bueno de ' + invitado)
                                                        if Fantasmas_malos2[iterador][1] == i-1 and Fantasmas_malos2[iterador][2] == x:
                                                            print("Entro al condicional fantasmas M")
                                                            Fantasmas_malos2[iterador][1] = 0
                                                            Fantasmas_malos2[iterador][2] = 0
                                                            Fantasmas_malos2[iterador][0] = 0
                                                            print('Has ahuyentado un fantasma malo de '+ invitado)
                                                print('Te moviste hacia la izquierda')
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x:
                                                       # print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                        Fantasmas_buenos1[iterador][1] = i-1
                                                        Fantasmas_buenos1[iterador][2] = x
                                                      #  print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                        
                                                    if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x:
                                                        Fantasmas_malos1[iterador][1] = i-1
                                                        Fantasmas_malos1[iterador][2] = x
                                                      
                                                        
                                                tablero[x][i-1] = "F1 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break


                                    elif opcion_mover == "4":
                                        if i == 7:
                                            print('No te puedes mover hacia la derecha')
                                        else:
                                            if tablero[x][i+1] == tablero[x][i]:
                                                print('Fuego amigo!')
                                            else:
                                                if tablero[x][i+1] == "F2 ":
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos2[iterador][1] == i+1 and Fantasmas_buenos2[iterador][2] == x:
                                                            Fantasmas_buenos2[iterador][0] = 0
                                                            Fantasmas_buenos2[iterador][1] = 0
                                                            Fantasmas_buenos2[iterador][2] = 0
                                                            print('Has ahuyentado un fantasma bueno de ' + invitado)
                                                        if Fantasmas_malos2[iterador][1] == i+1 and Fantasmas_malos2[iterador][2] == x:
                                                            Fantasmas_malos2[iterador][1] = 0
                                                            Fantasmas_malos2[iterador][2] = 0
                                                            Fantasmas_malos2[iterador][0] = 0
                                                            print('Has ahuyentado un fantasma malo de ' + invitado)
                                                print('Te moviste hacia la derecha')
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x:
                                                        Fantasmas_buenos1[iterador][1] = i+1
                                                        Fantasmas_buenos1[iterador][2] = x
                                                      #  print("Fantasma en x: "+ str(Fantasmas_buenos1[iterador][1]) + " en y:" + str(Fantasmas_buenos1[iterador][2]))
                                                        
                                                    if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x:
                                                        Fantasmas_malos1[iterador][1] = i+1
                                                        Fantasmas_malos1[iterador][2] = x
                                                        #print("Fantasma en x: "+ str(Fantasmas_malos1[iterador][1]) + " en y:" + str(Fantasmas_malos1[iterador][2]))
                                                tablero[x][i+1] = "F1 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break


                                    else:
                                        print("Escoja una opcion valida") 
                                
                                else:
                                    if opcion_mover == "1":
                                        if x == 2:
                                            print('No te puedes mover hacia arriba')
                                        else:
                                            if tablero[x][i] == tablero[x-1][i]:
                                                print('Fuego amigo!')
                                            else:
                                                if tablero[x-1][i] == "F1 ":
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x-1:
                                                            Fantasmas_buenos1[iterador][0] = 0
                                                            Fantasmas_buenos1[iterador][1] = 0
                                                            Fantasmas_buenos1[iterador][2] = 0
                                                            print('Has ahuyentado un fantasma bueno de ' + local)
                                                        if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x-1:
                                                            Fantasmas_malos1[iterador][1] = 0
                                                            Fantasmas_malos1[iterador][2] = 0
                                                            Fantasmas_malos1[iterador][0] = 0
                                                            print('Has ahuyentado un fantasma malo de ' + local)
                                                print('Te moviste hacia arriba')
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x:
                                                        Fantasmas_buenos2[iterador][1] = i
                                                        Fantasmas_buenos2[iterador][2] = x-1
                                                        print("Fantasma en x: "+ str(Fantasmas_buenos2[iterador][1]) + " en y:" + str(Fantasmas_buenos2[iterador][2]))
                                                    if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x:
                                                        Fantasmas_malos2[iterador][1] = i
                                                        Fantasmas_malos2[iterador][2] = x-1
                                                       # print("Fantasma en x: "+ str(Fantasmas_malos2[iterador][1]) + " en y:" + str(Fantasmas_malos2[iterador][2]))
                                                tablero[x-1][i] = "F2 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break

                                    elif opcion_mover == "2":
                                        if (x == 7 and i == 7) or (x == 7 and i == 2):
                                            for iterador in range(1, 5):
                                                if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x:
                                                    llave = 1
                                                    llave2 = 1
                                                    print("===========¡FELICIDADES! Ganador: JUGADOR " + invitado +  "============ ")
                                                    ganador = invitado
                                                    perdedor = local
                                                    jugador_gana = True
                                                    break
                                            if jugador_gana == True:
                                                break
                                        else:
                                            if x == 7:
                                                print('No te puedes mover hacia abajo')
                                            else:
                                                if tablero[x+1][i] == tablero[x][i]:
                                                    print('Fuego amigo!')
                                                else:
                                                    if tablero[x+1][i] == "F1 ":
                                                        for iterador in range(1, 5):
                                                            if Fantasmas_buenos1[iterador][1] == i and Fantasmas_buenos1[iterador][2] == x+1:
                                                                Fantasmas_buenos1[iterador][0] = 0
                                                                Fantasmas_buenos1[iterador][1] = 0
                                                                Fantasmas_buenos1[iterador][2] = 0
                                                                print('Has ahuyentado un fantasma bueno de '+ local)
                                                            if Fantasmas_malos1[iterador][1] == i and Fantasmas_malos1[iterador][2] == x+1:
                                                                Fantasmas_malos1[iterador][1] = 0
                                                                Fantasmas_malos1[iterador][2] = 0
                                                                Fantasmas_malos1[iterador][0] = 0
                                                                print('Has ahuyentado un fantasma malo de '+ local)
                                                    print('Te moviste hacia abajo')
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x:
                                                            Fantasmas_buenos2[iterador][1] = i
                                                            Fantasmas_buenos2[iterador][2] = x+1
                                                           # print("Fantasma en x: "+ str(Fantasmas_buenos2[iterador][1]) + " en y:" + str(Fantasmas_buenos2[iterador][2]))
                                                        if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x:
                                                            Fantasmas_malos2[iterador][1] = i
                                                            Fantasmas_malos2[iterador][2] = x+1
                                                           # print("Fantasma en x: "+ str(Fantasmas_malos2[iterador][1]) + " en y:" + str(Fantasmas_malos2[iterador][2]))
                                                    tablero[x+1][i] = "F2 "
                                                    tablero[x][i] = " " + "_" + " "
                                                    llave2 = 1
                                                    break


                                    elif opcion_mover == "3":
                                        if i == 2:
                                            print('No te puedes mover hacia la izquierda')
                                        else:
                                            if tablero[x][i-1] == tablero[x][i]:
                                                print('Fuego amigo!')
                                            else:
                                               
                                                if tablero[x][i-1] == "F1 ":
                                                   
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos1[iterador][1] == i-1 and Fantasmas_buenos1[iterador][2] == x:
                                                            
                                                            Fantasmas_buenos1[iterador][0] = 0
                                                            Fantasmas_buenos1[iterador][1] = 0
                                                            Fantasmas_buenos1[iterador][2] = 0
                                                            print('Has ahuyentado un fantasma bueno de '+ local)
                                                        if Fantasmas_malos1[iterador][1] == i-1 and Fantasmas_malos1[iterador][2] == x:
                                                            
                                                            Fantasmas_malos1[iterador][1] = 0
                                                            Fantasmas_malos1[iterador][2] = 0
                                                            Fantasmas_malos1[iterador][0] = 0
                                                            print('Has ahuyentado un fantasma malo de '+ local)
                                                print('Te moviste hacia la izquierda')
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x:
                                                        Fantasmas_buenos2[iterador][1] = i-1
                                                        Fantasmas_buenos2[iterador][2] = x
                                                        print("Fantasma en x: "+ str(Fantasmas_buenos2[iterador][1]) + " en y:" + str(Fantasmas_buenos2[iterador][2]))
                                                        
                                                    if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x:
                                                        Fantasmas_malos2[iterador][1] = i-1
                                                        Fantasmas_malos2[iterador][2] = x
                                                        print("Fantasma en x: "+ str(Fantasmas_malos2[iterador][1]) + " en y:" + str(Fantasmas_malos2[iterador][2]))
                                                            
                                                tablero[x][i-1] = "F2 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                        
                                                break


                                    elif opcion_mover == "4":

                                        if i == 7:
                                            print('No te puedes mover hacia la derecha')
                                        else:
                                            if tablero[x][i+1] == tablero[x][i]:
                                                print('Fuego amigo!')
                                            else:
                                                if tablero[x][i+1] == "F1 ":
                                                    for iterador in range(1, 5):
                                                        if Fantasmas_buenos1[iterador][1] == i+1 and Fantasmas_buenos1[iterador][2] == x:
                                                            Fantasmas_buenos1[iterador][0] = 0
                                                            Fantasmas_buenos1[iterador][1] = 0
                                                            Fantasmas_buenos1[iterador][2] = 0
                                                            print('Has ahuyentado un fantasma bueno de '+ local)
                                                        if Fantasmas_malos1[iterador][1] == i+1 and Fantasmas_malos1[iterador][2] == x:
                                                            Fantasmas_malos1[iterador][1] = 0
                                                            Fantasmas_malos1[iterador][2] = 0
                                                            Fantasmas_malos1[iterador][0] = 0
                                                            print('Has ahuyentado un fantasma malo de '+ local)
                                                print('Te moviste hacia la derecha')
                                                for iterador in range(1, 5):
                                                    if Fantasmas_buenos2[iterador][1] == i and Fantasmas_buenos2[iterador][2] == x:
                                                        Fantasmas_buenos2[iterador][1] = i+1
                                                        Fantasmas_buenos2[iterador][2] = x
                                                        print("Fantasma en x: "+ str(Fantasmas_buenos2[iterador][1]) + " en y:" + str(Fantasmas_buenos2[iterador][2]))
                                                    if Fantasmas_malos2[iterador][1] == i and Fantasmas_malos2[iterador][2] == x:
                                                        Fantasmas_malos2[iterador][1] = i+1
                                                        Fantasmas_malos2[iterador][2] = x
                                                        print("Fantasma en x: "+ str(Fantasmas_malos2[iterador][1]) + " en y:" + str(Fantasmas_malos2[iterador][2]))
                                                tablero[x][i+1] = "F2 "
                                                tablero[x][i] = " " + "_" + " "
                                                llave2 = 1
                                                break


                                    else:
                                        print("Opcion invalida")


                            if jugador == 1:
                                jugador = 2
                            else:
                                jugador = 1   
                            

                            
                            totalFantasma = 0

                            
                            for iterador in range(1, 5):
                                totalFantasma += Fantasmas_buenos1[iterador][0]
                            fantasmaBuenoTotal1 = totalFantasma

                            
                            if totalFantasma == 0:
                                
                                print("===========FELICIDADES! Ganador: JUGADOR " + invitado +  "============ ")
                                ganador = invitado
                                perdedor = local
                                llave = 1

                            totalFantasma = 0

                            
                            for iterador in range(1, 5):
                                totalFantasma += Fantasmas_buenos2[iterador][0]
                            fantasmaBuenoTotal2 = totalFantasma

                           
                            if totalFantasma == 0:
                                
                                print("===========FELICIDADES! Ganador: JUGADOR " + local +  "============ ")
                                ganador = local
                                perdedor = invitado
                                llave = 1

                            totalFantasma = 0

                            
                            for iterador in range(1, 5):
                                totalFantasma += Fantasmas_malos1[iterador][0]
                            fantasmaMaloTotal1 = totalFantasma

                            
                            if totalFantasma == 0:
                                
                                print("===========FELICIDADES! Ganador: JUGADOR " + local +  "============ ")
                                ganador = local
                                perdedor = invitado
                                llave = 1

                            totalFantasma = 0

                            
                            for iterador in range(1, 5):
                                totalFantasma += Fantasmas_malos2[iterador][0]
                            fantasmaMaloTotal2 = totalFantasma

                            
                            if totalFantasma == 0:
                                print("===========FELICIDADES! Ganador: JUGADOR " + invitado +  "============ ")
                                ganador = invitado
                                perdedor = local
                                llave = 1

                    
                    pos = 0

                    while pos < cantidad_usuarios_creados:
                        if usernames[pos] == ganador:
                            puntos[pos] += 3
                            totalVictorias[pos] += 1
                            for iterador in range((10 * (pos+1))-1, (pos * 10)-1, -1):
                                
                                if iterador == (10 * (pos+1))-1:
                                    partidas[(10 * (pos+1))-1] = ""
                                elif iterador == (pos * 10):
                                    
                                    partidas[(pos * 10)] = "Victoria"
                                else:
                                    partidas[iterador] = partidas[iterador - 1]
                        pos += 1

                    pos = 0

                    while pos < cantidad_usuarios_creados:
                        if usernames[pos] == perdedor:
                            totalDerrotas[pos] += 1
                            for iterador in range((10 * (pos+1))-1, (pos * 10)-1, -1):
                                
                                if iterador == (10 * (pos+1))-1:
                                    
                                    partidas[(10 * (pos+1))-1] = ""
                                elif iterador == (pos * 10):
                                    
                                    partidas[(pos * 10)] = "Derrota"
                                else:
                                    
                                    partidas[iterador] = partidas[iterador - 1]
                        pos += 1

                elif opcion_menu_sesion == 2: 
                    print("1. Dificultad")
                    print("2. Modo de juego")
                    print("3. Regresar al menú principal")
                    config = int(input())

                    if config == 1:
                        print("1. Normal")
                        print("2. Experto")
                        print("3. Genio")
                        config = int(input())
                        if config == 1:
                            llaveConfig = 1
                        elif config == 2:
                            llaveConfig = 2
                        elif config == 3:
                            llaveConfig = 3
                        else:
                            print("Error")
                    elif config == 2:
                        print("1. Aleatorio")
                        print("2. Manual")
                        llaveConfig2 = int(input())
                    elif config == 3:
                        print("Volviendo..")
                    else:
                        print("Opción inválida")


                elif opcion_menu_sesion == 3: 
                    print("1. Descripción de mis últimos 10 juegos")
                    print("2. Mejores jugadores")
                    print("3. Exportar datos a Excel")
                    print("4. Regresar")
                    respuesta = int(input())

                    if respuesta == 1:
                        
                        print("ÚLTIMAS PARTIDAS DEL JUGADOR: " + local)
                        aux = 1
                        pos = 0  # Empezamos desde 0
                        while pos < cantidad_usuarios_creados:
                            if usernames[pos] == local:
                                for iterador in range(pos * 10, (pos + 1) * 10):
                                    if partidas[iterador] != "":
                                        print(str(aux) + ". " + partidas[iterador])
                                        aux += 1
                                mostrar_grafico(totalVictorias[pos], totalDerrotas[pos])
                            pos += 1
                        

                        
                    elif respuesta == 2:
                        usernames_copia = usernames[:]
                        puntos_copia = puntos[:]
                        for i in range(cantidad_usuarios_creados):
                            for j in range(i + 1, cantidad_usuarios_creados):
                                if puntos[i] < puntos[j]:
                                    
                                    temp_puntaje = puntos_copia[i]
                                    puntos_copia[i] = puntos_copia[j]
                                    puntos_copia[j] = temp_puntaje
                                    
                                    temp_nombre = usernames_copia[i]
                                    usernames_copia[i] = usernames[j]
                                    usernames_copia[j] = temp_nombre

                        print("Mejores jugadores:")
                        for i in range(cantidad_usuarios_creados):
                            if puntos[i] > 0:
                                print(usernames[i], ": ", puntos[i])


                        mostrar_grafico_puntaje(usernames, puntos)

                    elif respuesta == 3:
                        if verificarSiJuegoExiste(local):
                            break
                        for i in range(cantidad_usuarios_creados):
                            if usernames[i] == local:
                                exportar_grafico2 = devolver_grafico_puntaje(usernames, puntos)
                                exportar_grafico1 = devolver_grafico(totalVictorias[i], totalDerrotas[i])
                                
                                guardar_datos_y_graficos_en_excel(usernames[i],nombres_completos[i],edades[i],numeros_cuentas[i],exportar_grafico1,exportar_grafico2)


                    elif respuesta == 4:
                        print("Saliendo")
                    else:
                        print("Fuera de rango")


                elif opcion_menu_sesion == 4: 
                    print("1. Ver mis datos")
                    print("2. Cambiar contraseña")
                    print("3. Eliminar mi cuenta")
                    print("4. Regresar")
                    respuesta = int(input())

                    if respuesta == 1:
                        pos = 0
                        while pos < cantidad_usuarios_creados:
                            if usernames[pos] == local:
                                print("Nombre: " + nombres_completos[pos])
                                print("Numero de cuenta: " + numeros_cuentas[pos])
                                print("Edad: " + str(edades[pos]))
                                print("Username: " + usernames[pos])
                                print("Contraseña: " + passwords[pos])
                                print("Total Victorias: " + str(totalVictorias[pos]))
                                print("Total Derrotas: " + str(totalDerrotas[pos]))
                                print("Puntaje total: " + str(puntos[pos]))
                            pos += 1
                    elif respuesta == 2:
                        print("Ingrese contraseña vieja: ", end="")
                        password_login = input()

                        pos = 0
                        while pos < cantidad_usuarios_creados:
                            if usernames[pos] == local and passwords[pos] == password_login:
                                print("Ingrese contraseña nueva")
                                password_login = input()

                                print("¿Está seguro de que quiere actualizar la contraseña?")
                                print("1. Si")
                                print("2. No")
                                respuesta = int(input())

                                if respuesta == 1:
                                    passwords[pos] = password_login
                                    print("Contraseña actualizada correctamente")
                                elif respuesta == 2:
                                    print("Volviendo al menú")
                                else:
                                    print("Fuera de rango")
                            pos += 1
                    elif respuesta == 3:
                        print("¿Está seguro de que quiere eliminar su cuenta?")
                        print("1. Si")
                        print("2. No")
                        respuesta = int(input())

                        if respuesta == 1:
                            print("Ingrese contraseña")
                            password_login = input()
                            pos = 0
                            while pos < cantidad_usuarios_creados:
                                if usernames[pos] == local and passwords[pos] == password_login:
                                    aux = 1
                                    numeros_cuentas[pos] = ""
                                    nombres_completos[pos] = ""
                                    edades[pos] = 0
                                    usernames[pos] = ""
                                    passwords[pos] = ""
                                    puntos[pos] = 0
                                    totalDerrotas[pos] = 0
                                    totalVictorias[pos] = 0
                                    for j in range((pos * 10), (pos +1 ) * 10):
                                        partidas[j] = ""
                                    for i in range(pos, cantidad_usuarios_creados-1):
                                        numeros_cuentas[i] = numeros_cuentas[i + 1]
                                        nombres_completos[i] = nombres_completos[i + 1]
                                        edades[i] = edades[i + 1]
                                        usernames[i] = usernames[i + 1]
                                        passwords[i] = passwords[i + 1]
                                        puntos[i] = puntos[i + 1]
                                        totalDerrotas[i] = totalDerrotas[i + 1]
                                        totalVictorias[i] = totalVictorias[i + 1]
                                        for j in range(10):
                                            partidas[((i) * 10) + j] = partidas[((i+1) * 10) + j]
                                    if aux != -1:
                                        cantidad_usuarios_creados -= 1
                                        numeros_cuentas.pop()
                                        nombres_completos.pop()
                                        edades.pop()
                                        usernames.pop()
                                        passwords.pop()
                                        puntos.pop()
                                        totalDerrotas.pop()
                                        totalVictorias.pop()
                                        partidas = partidas[:-10]
                                        
                                        eliminar_usuario(local)
                                        print("Cuenta eliminada")
                                        menu_sesion = False
                                else:
                                    if usernames[pos] == local and passwords[pos] != password_login:
                                        print("Error al borrar cuenta")
                                        aux = -1
                                pos += 1
                            
                        elif respuesta == 2:
                            print("Volviendo al menú")
                        else:
                            print("Valor inválido")
                    elif respuesta == 4:
                        print("Saliendo")
                    else:
                        print("Fuera de rango")


                elif opcion_menu_sesion == 5: 
                    print("Saliendo...")
                    break

                
                else:
                    print("Opcion invalida")

        else:
            print("¡Ha ingresado un nombre de usuario/contraseña incorrecto!")

    elif opcion_menu_principal == 2:
        valido = True
        pos = 1

        print("")
        print("*** CREAR PLAYER ***")
        print("Ingrese su número de cuenta: ", end="")
        nuevo_num_cuenta = input()
        

        while pos < cantidad_usuarios_creados:
            if numeros_cuentas[pos-1] == nuevo_num_cuenta:
                print("¡Ese número de cuenta ya existe!")
                valido = False
            pos = pos + 1

        if valido:
            print("Ingrese su nombre completo: ", end="")
            nuevo_nombre_completo = input()
            
            print("Ingrese su edad: ", end="")
            nuevo_edad = int(input())
            
            if nuevo_edad <= 12 or nuevo_edad > 70:
                print("¡Ingrese una edad correcta!")
                print("")
            else:
                print("Ingrese un username: ", end="")
                nuevo_username = input()
                
                pos = 1
                while pos < cantidad_usuarios_creados:
                    if usernames[pos-1] == nuevo_username:
                        print("¡Ese username ya existe!")
                        valido = False
                    pos = pos + 1
                
                if valido:
                    print("Ingrese una contraseña: ", end="")
                    nuevo_password = input()
                    
                    usuario_creado = crear_usuario(nuevo_num_cuenta, nuevo_nombre_completo, nuevo_edad, nuevo_username, nuevo_password)
                    if usuario_creado == True:
                        numeros_cuentas.append(nuevo_num_cuenta)
                        nombres_completos.append(nuevo_nombre_completo)
                        edades.append(nuevo_edad)
                        usernames.append(nuevo_username)
                        passwords.append(nuevo_password)
                        puntos.append(0)
                        totalVictorias.append(0)
                        totalDerrotas.append(0)
                        for i in range(10):
                            partidas.append("")
                        cantidad_usuarios_creados = cantidad_usuarios_creados + 1
                        print("")
                        print("¡Se ha creado exitosamente el usuario!")
                        print("")
                        
    elif opcion_menu_principal == 3:
        print("")
        print("¡HA SALIDO!")
        menu_principal = False


    else: 
        print("Fuera de rango")