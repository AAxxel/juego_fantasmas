import os

def eliminar_usuario(username):

    ruta_archivo_usuario = os.path.join('usuarios', f'{username}.txt')
    if not os.path.exists(ruta_archivo_usuario):
        print(f"El usuario '{username}' no existe.")
        return False


    os.remove(ruta_archivo_usuario)
    print(f"El archivo del usuario '{username}' ha sido eliminado correctamente.")

   
    ruta_archivo_nombres = 'nombres_usuarios.txt'
    with open(ruta_archivo_nombres, 'r') as archivo_nombres:
        nombres_usuarios = archivo_nombres.readlines()

    with open(ruta_archivo_nombres, 'w') as archivo_nombres:
        for nombre in nombres_usuarios:
            if nombre.strip() != username:
                archivo_nombres.write(nombre)

  
    ruta_archivo_numeros = 'numeros_cuenta.txt'
    with open(ruta_archivo_numeros, 'r') as archivo_numeros:
        numeros_cuenta = archivo_numeros.readlines()

    with open(ruta_archivo_numeros, 'w') as archivo_numeros:
        for numero in numeros_cuenta:
            if numero.strip() != username:
                archivo_numeros.write(numero)

    return True