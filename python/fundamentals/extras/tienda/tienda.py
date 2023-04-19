class tiendita:
    def __init__(self, name):
        self.nombre = name
        self.producto = []


    def add_producto(self,produc):
        self.producto.append(produc)
        return self
    def Print_info(self):
        for i in self.producto:
            print(f"{ i.nombre} {i.precio} {i.categoria} ")
        return self