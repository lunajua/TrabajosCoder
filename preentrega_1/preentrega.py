"""Crear un programa que permita emular el registro y almacenamiento de usuarios en una base 
de datos. Crear el programa utilizando el concepto de funciones, diccionarios, bucles y 
condicionales.
El formato de registro es: Nombre de usuario y Contraseña.
✓ Utilizar una función para almacenar la información y otra función para mostrar la información.
✓ Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña 
(clave-valor).
✓ Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el 
usuario"""

bd = {}

def registro():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    bd[usuario] = contrasena
    print("Registro exitoso.")
    print(bd)

def mostrar_registros():
    print(bd)
    for usuario, contrasena in bd.items():
        print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    print("Registros mostrados.")
    print(bd)
    
    #for usuario in bd:
    #    print(f"Usuario: {usuario}, Contraseña: {bd[usuario]}")
    #print("Registros mostrados.")
    #print(bd)
    
    #for usuario in bd.keys():
    #    print(f"Usuario: {usuario}, Contraseña: {bd[usuario]}")
    #print("Registros mostrados.")
    #print(bd)
    
    #for contrasena in bd.values():
    #    print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    #print("Registros mostrados.")
    #print(bd)
    
    #for usuario, contrasena in bd.items(): 
    
def login():
    usuario = input("Ingrese usuario: ")
    contrasena = input("Ingrese contraseña: ")
    if usuario in bd and bd[usuario] == contrasena:
        print("Login exitoso.")
    else:
        print("Login fallido.")

ultimo_archivo = None

def guardar_bd():
    global ultimo_archivo
    if ultimo_archivo is not None:
        print(f"El último nombre fue: {ultimo_archivo}")
    archivo = input("Ingrese nombre del archivo con su extensión: ")
    ultimo_archivo = archivo
    with open(archivo, "a", encoding="UTF-8") as f:
        for usuario, contrasena in bd.items():
            f.write(f"{usuario},{contrasena}\n")

            
def cargar_bd():
    archivo = input("Ingrese nombre del archivo a visualizar con su extensión: ")
    try:
        with open(archivo, "r", encoding="UTF-8") as f:
            for linea in f:
                usuario, contrasena = linea.strip().split(",")
                bd[usuario] = contrasena
                print(f"Usuario: {usuario}, Contraseña: {contrasena}")
    except FileNotFoundError:
        print("Error al cargar el archivo ó archivo inexistente.") 

def menu():
    flag = True        
    while flag:
             
        opcion = input("""
                       
Ingrese:

            1 Para registrar 
            2 Para login 
            3 Guardar datos en archivo 
            4 Mostrar registros almacenados
            5 Mostrar archivo guarddo 
            6 Salida del sistema 
                
            Ingrese la opción deseada:  """)
        
            
        try:
            if opcion == "1":
                registro()
            elif opcion == "2":
                login()    
            elif opcion == "3":
                guardar_bd()
            elif opcion == "4":
                mostrar_registros()
            elif opcion == "5":
                cargar_bd()
            elif opcion == "6":
                print()
                print("Saliendo del programa")
                flag = False
        
        except ValueError:        
            print("Opción inválida.")
        
        
if __name__ == "__main__":
    menu()        