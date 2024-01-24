from .modulo1 import Cliente
from .modulo1 import ClienteInvalido


def registrar():
    while True:
        try:
            nombre = input("Ingrese nombre: ").capitalize()
            direccion = input("Ingrese dirección de entrega: ")
            email = input("Ingrese email: ")
            carrito_de_compras = []  # Inicializa la lista vacía
            return Cliente(nombre, direccion, email, carrito_de_compras)
        except ClienteInvalido as e:
            print(str(e))  # Imprime el mensaje de error


# def registrar():
#     while True:
#         try:
            
#             nombre = input("Ingrese nombre: ").capitalize()
#             if not nombre:  # Verifica que el nombre no esté vacío
#                 print("El nombre no puede estar vacío.")
#                 continue

#             direccion = input("Ingrese dirección de entrega: ")
#             if not direccion:  # Verifica que la dirección no esté vacía
#                 print("La dirección no puede estar vacía.")
#                 continue

#             email = input("Ingrese email: ")
#             if not email:  # Verifica que el email no esté vacío
#                 print("El email no puede estar vacío.")
#                 continue
#             elif '@' not in email or '.' not in email:  # Verifica que el email sea válido
#                 print("Por favor, ingrese un email válido.")
#                 continue

#             carrito_de_compras = []  # Inicializa la lista vacía
#             return Cliente(nombre, direccion, email, carrito_de_compras)
        
#         except ClienteInvalido as e:
#             print(str(e))  # Imprime el mensaje de error


def agregar_producto(cliente):
    while True:
        producto = input("Ingrese producto: ")
        cliente.agregar_al_carrito(producto)
        question = input("¿Desea agregar otro producto al carrito de compras? (S/N): ").lower()
        if question != "s":
            break

# Veo los productos en el carrito con el método ver_carrito 
def ver_carrito(cliente):
    return cliente.carrito_de_compras

# Imprime los detalles del cliente con el método __str__
def imprimir_cliente(cliente):
    return str(cliente)