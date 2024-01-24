from .modulo1 import Cliente #Al ser una importación relativa uso el punto porque modulo 1 y modulo 2 están en el mismo paquete

# Creo un cliente con el método registrar
def registrar():
    nombre = input("Ingrese nombre: ").capitalize()
    direccion = input("Ingrese dirección de entrega: ")
    email = input("Ingrese email: ")
    carrito_de_compras = []  # Inicializo la lista vacía
    return Cliente(nombre, direccion, email, carrito_de_compras)


# Agrego un producto al carrito con el método agregar_al_carrito
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


