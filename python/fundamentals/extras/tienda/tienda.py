class tiendita:
    def __init__(self, name):
        self.nombre = name
        self.producto = []

    def add_producto(self, produc):
        self.producto.append(produc)
        return self

    def Print_info(self):
        for i in self.producto:
            print(f"{ i.nombre} {i.precio} {i.categoria} ")
        return self
    
    def vender(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n

    def inflacion(self, porcentaje , *nums):
            self.result -= porcentaje    
            for n in nums:
                self.result += n

    def hacer_liquidacion(self, num, *nums):
            self.result -= num
            for n in nums:
                self.result -= n