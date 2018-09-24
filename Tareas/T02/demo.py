from gui.entities import Entity, Human
import gui
import os

_PATH = os.path.dirname(os.path.abspath(__file__))

gui.init()

client = Human("millonario")
client.add_decoration("gui/assets/decoracion/bullet.png")

client.angle = 0
client.y = 0
client.x = 0
ticks = 0


def tick():
    client.x += 1
    client.y += 1
    client.angle += 1

gui.set_size(773, 485)
gui.add_entity(client)
gui.run(tick, 50)
