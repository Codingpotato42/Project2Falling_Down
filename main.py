from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina application
app = Ursina()

# Create a large ground plane
# We use a plane model, scale it up, give it a simple color and texture,
# and add a 'mesh' collider so the player can walk on it.
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.rgb(140, 140, 140), # A gray color
    texture='white_cube',
    texture_scale=(100, 100), # Tile the texture
    collider='mesh'
)

# Add a simple skybox to make the scene feel less empty
Sky()

# Add the FirstPersonController
# We set its initial position slightly above the ground
player = FirstPersonController(
    position=(0, 1, 0),
    speed=8
)

# Function to handle input
def input(key):
    # Check if the pressed key is 'escape'
    if key == 'escape':
        quit()  # Quit the application

# Run the application
app.run()
