class ClienteInvalido(Exception):
    pass

class Cliente:
    def __init__(self, nombre, direccion, email, carrito_de_compras):
        if not nombre or not direccion or not email:
            raise ClienteInvalido("Nombre, dirección y email son requeridos.")        
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.carrito_de_compras = carrito_de_compras