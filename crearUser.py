import os

def verificar_existencia(nombre_usuario, numero_cuenta):

    ruta_nombre_usuario = 'nombres_usuarios.txt'
    ruta_numeros_cuenta = 'numeros_cuenta.txt'

    
    if not os.path.exists(ruta_nombre_usuario):
        with open(ruta_nombre_usuario, 'w') as archivo_nombres:
            pass

    
    if not os.path.exists(ruta_numeros_cuenta):
        with open(ruta_numeros_cuenta, 'w') as archivo_numeros:
            pass

    
    with open(ruta_nombre_usuario, 'r') as archivo_nombres:
        nombres_usuarios = archivo_nombres.readlines()
        nombres_usuarios = [nombre.strip() for nombre in nombres_usuarios]
        if nombre_usuario in nombres_usuarios:
            print("¡El nombre de usuario ya existe! Por favor, ingrese otro nombre de usuario.")
            return True

   
    with open(ruta_numeros_cuenta, 'r') as archivo_numeros:
        numeros_cuenta = archivo_numeros.readlines()
        numeros_cuenta = [numero.strip() for numero in numeros_cuenta]
        if numero_cuenta in numeros_cuenta:
            print("¡El número de cuenta ya existe! Por favor, ingrese otro número de cuenta.")
            return True

    return False

def crear_usuario(numero_cuenta, nombre, edad, username, contraseña):
   
    if verificar_existencia(username, numero_cuenta):
        return False

    
    carpeta_usuarios = 'usuarios'
    if not os.path.exists(carpeta_usuarios):
        os.makedirs(carpeta_usuarios)


    with open(os.path.join(carpeta_usuarios, f'{username}.txt'), 'w') as archivo_usuario:
        archivo_usuario.write(f"Nombre: {nombre}\n")
        archivo_usuario.write(f"Edad: {edad}\n")
        archivo_usuario.write(f"Contraseña: {contraseña}\n")
        archivo_usuario.write(f"Nombre de usuario: {username}\n")
        archivo_usuario.write(f"Número de cuenta: {numero_cuenta}\n")

  
    with open('nombres_usuarios.txt', 'a') as archivo_nombres:
        archivo_nombres.write(f"{username}\n")

   
    with open('numeros_cuenta.txt', 'a') as archivo_numeros:
        archivo_numeros.write(f"{numero_cuenta}\n")

    return True
