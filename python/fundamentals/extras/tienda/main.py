from tienda import tiendita
from producto import productito

tienda1 = tiendita(name="Unbimarc")
producto1 = productito(name="camiseta U", impor=2500000, cat="deporte")
producto2 = productito(name="camiseta X", impor=25, cat="deporte")
producto3 = productito(name="camiseta Monja", impor=25, cat="deporte")
producto4 = productito(name="camiseta Cobreloa", impor=2500, cat="deporte")

tienda1.add_producto(producto1)
tienda1.add_producto(producto2)
tienda1.add_producto(producto3)
tienda1.add_producto(producto4)

tienda1.Print_info()