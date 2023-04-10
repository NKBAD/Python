import random

class Baraja:
    def __init__(self):
        # Crear baraja
        figuras = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        valores = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jota', 'Reina', 'Rey']
        self.baraja = []
        for figuras in figuras:
            for valor in valores:
                self.baraja.append((valor, figuras))

    def mezclar(self):
        # Mezclar la baraja
        random.shuffle(self.baraja)

    def sacar_carta(self):
        # Sacar una carta de la baraja
        return self.baraja.pop()

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def tomar_carta(self, carta):
        # Agregar carta a la mano del jugador
        self.mano.append(carta)

    def mostrar_mano(self):
        # Mostrar cartas en la mano del jugador
        print(self.nombre + "'s mano:")
        for carta in self.mano:
            print('  ' + carta[0] + ' de ' + carta[1])

    def valor_mano(self):
        # Calcular valor total de la mano del jugador
        valores = {'As': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jota': 10, 'Reina': 10, 'Rey': 10}
        total = 0
        ases = 0
        for carta in self.mano:
            valor = carta[0]
            if valor == 'As':
                ases += 1
            total += valores[valor]
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        return total

# Crear baraja y mezclarla
baraja = Baraja()
baraja.mezclar()

# Crear dos jugadores
nico = Jugador('nacho')
diego = Jugador('dilan')

# Repartir dos cartas a cada jugador
nico.tomar_carta(baraja.sacar_carta())
nico.tomar_carta(baraja.sacar_carta())
diego.tomar_carta(baraja.sacar_carta())
diego.tomar_carta(baraja.sacar_carta())

# Mostrar cartas de nico y una carta de dilan
nico.mostrar_mano()
print(' ')
print("diego's mano:")
print('  ' + diego.mano[0][0] + ' de ' + diego.mano[0][1])

# Pedir al jugador que opte por más cartas
while True:
    opcion = input("Quieres tomar otra carta? (s/n) ")
    if opcion.lower() == 's':
        nico.tomar_carta(baraja.sacar_carta())
        nico.mostrar_mano()
        if nico.valor_mano() > 21:
            print('Te has pasado de 21. Perdiste.')
            quit()
    else:
        break

# Jugada de diego
diego.mostrar_mano()
while diego.valor_mano() < 17:
    diego.tomar_carta(baraja.sacar_carta())
    diego.mostrar_mano()

# Comparar manos
nico_total = nico.valor_mano()
diego_total = diego.valor_mano()
print(' ')
print("Puntajes:")
print(nico.nombre + ': ' + str(nico_total))
print(diego.nombre + ': ' + str(diego_total))
if nico_total > diego_total:
    print(nico.nombre + ' gana!')
elif diego_total > nico_total:
    print(diego.nombre + ' gana!')
else:
    print('Empate!')