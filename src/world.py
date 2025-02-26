from ursina import *

# 🔹 Uruchamiamy Ursina
app = Ursina()

# Tworzymy światło i niebo
Sky()
DirectionalLight(direction=(1, 1, 1), color=color.white)

# 🔹 Tworzymy planszę 3D (10x10)
ROWS, COLS = 10, 10
CELL_SIZE = 2  # Rozmiar pól

grid = []

for x in range(ROWS):
    for z in range(COLS):
        tile = Entity(
            model="cube",
            color=color.green,
            texture="white_cube",
            scale=(CELL_SIZE, 0.2, CELL_SIZE),
            position=(x * CELL_SIZE, 0, z * CELL_SIZE)
        )
        grid.append(tile)

# 🔹 Uruchomienie aplikacji
app.run()