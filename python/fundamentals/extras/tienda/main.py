from tienda import tiendita 
from producto import productito

tienda1 = tiendita(name="Unbimarc")
producto1 = productito(name="camiseta U",impor=65000,cat="deporte")
producto2 = productito(name="Balon de fútbol",impor=25000,cat="deporte")
producto3 = productito(name="Zapatos running",impor=60000,cat="deporte")
producto4 = productito(name="zapatos fútbol",impor=100000,cat="deporte")

tienda1.add_producto(producto1) 
tienda1.add_producto(producto2)
tienda1.add_producto(producto3)
tienda1.add_producto(producto4)

tienda1.Print_info()