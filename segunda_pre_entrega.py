from preentrega_2.paquete1.modulo1 import Cliente
from preentrega_2.paquete1.modulo2 import *
import time 
import os

def clear():
    time.sleep(1)
    os.system('cls')

def menu():
    clientes = {}
    clear()
    flag = True           
    while flag:
             
        opcion = input("""
                       
Ingrese:

            1 Registro de Cliente
            2 Visualizar datos del cliente
            3 Carrito de Compra
            4 Mostrar Carrito de Compra            
            5 Salida del sistema 
                
            Ingrese la opción deseada:  """)
        
        clear()    
        
        if opcion == "1":
            while True:
                cliente1 = registrar()
                clientes[cliente1.nombre] = cliente1 #Agrega el cliente al diccionario clientes
                question = input("Desea agregar otro cliente? S/N: ").lower()
                if question != "s":
                    print("Cliente registrado exitosamente")
                    break
        elif opcion in ["2", "3", "4"]:
            if not clientes: #Sino lo encuentra en el diccionario clientes, retorna False. Si lo encuentra, retorna un valor de True. 
                #Si no hay clientes, imprime un mensaje de error y regresa al menu principal. Si hay clientes, continua con el programa.                                 
                print("No hay clientes registrados. Registre un cliente por favor")                    
            else:
                nombre_cliente = input("Ingrese el nombre del cliente: ").capitalize()
                cliente = clientes.get(nombre_cliente) #Obtiene el cliente del diccionario clientes
                if opcion == "2":
                    print(imprimir_cliente(cliente))
                elif opcion == "3":
                    agregar_producto(cliente)
                elif opcion == "4":
                    print(ver_carrito(cliente))             
        elif opcion == "5":
            print()
            print("Saliendo del programa")
            flag = False        
        else:        
            print("Opción inválida.")
        
        
if __name__ == "__main__":
    menu()        

