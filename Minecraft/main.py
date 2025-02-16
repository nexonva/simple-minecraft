from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Block texture list
block_types = ['grass', 'brick', 'white_cube']
current_block = 0  # Selected block type

# UI Text
block_text = Text(text=f'Block: {block_types[current_block]}', position=(-0.5, 0.45), scale=2)

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture='grass'):
        super().__init__(
            parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture=texture,
            color=color.color(0, 0, random.uniform(0.9, 1.0)),
            highlight_color=color.lime
        )

# Create ground (10x1x10)
for z in range(10):
    for x in range(10):
        Voxel(position=(x, 0, z), texture='grass')

# Create player
player = FirstPersonController()
player.gravity = 1  # Enable gravity
player.jump_height = 1.5  # Set jump height

def update():
    player.speed = 10  # Movement speed

def input(key):
    global current_block
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal, texture=block_types[current_block])
    
    if key == 'right mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)
    
    # Block switching (number keys 1-3)
    if key in ['1', '2', '3']:
        current_block = int(key) - 1
        block_text.text = f'Block: {block_types[current_block]}'

app.run()
