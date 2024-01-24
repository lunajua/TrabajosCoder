class Cliente:
    def __init__(self, nombre, direccion, email, carrito_de_compras):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.carrito_de_compras = carrito_de_compras  
        
    #Utilizo el método extend para agregar al final de la lista los productos del carrito     
    def agregar_al_carrito(self, producto):
        self.carrito_de_compras.append(producto)

    def ver_carrito(self):
        return self.carrito_de_compras

    def __str__(self):
        return f'Cliente: {self.nombre}, Dirección: {self.direccion}, Email: {self.email}'

