from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# --- Iteration 4: Custom Gravity ---
# We define our own class for a cube that knows how to fall.
# It inherits from Entity, so it's still a 3D object.
class FallingCube(Entity):
    def __init__(self, **kwargs):
        # We call the parent's init function
        # This passes along model, texture, position, etc.
        super().__init__(**kwargs)
        
        # Our custom physics properties
        self.velocity_y = 0       # Its current downward speed
        self.is_grounded = False  # An optimization to stop checking once it lands
        self.gravity = 9.8        # How strong gravity is

    # update() is called automatically by Ursina every frame
    def update(self):
        # If the cube is already on the ground, do nothing.
        # This is a great optimization.
        if self.is_grounded:
            return

        # --- Apply Gravity ---
        # 1. Increase downward velocity over time.
        #    time.dt is the time since the last frame.
        self.velocity_y -= self.gravity * time.dt
        
        # 2. Apply the velocity to the cube's y (vertical) position.
        self.y += self.velocity_y * time.dt

        # --- Check for Ground Collision ---
        # A 1-unit cube's origin is its center. Its bottom is at y - 0.5.
        # The ground is at y = 0.
        if self.y <= 0.5:
            self.y = 0.5             # Set its position exactly on the ground
            self.velocity_y = 0      # Stop its velocity
            self.is_grounded = True  # Set its state to "grounded"
# --- End of Custom Gravity Class ---


# Initialize the Ursina application
app = Ursina()

# Create a large ground plane
# Note: We have removed all 'rigidbody' components.
ground = Entity(
    model='plane',
    scale=(100, 1, 100),
    color=color.rgb(140, 140, 140), # A gray color
    texture='white_cube',
    texture_scale=(100, 100), # Tile the texture
    collider='mesh' # The player still collides with this
)

# Add a simple skybox
Sky()

# Add the FirstPersonController
player = FirstPersonController(
    position=(0, 1, 0),
    speed=8,
    # We must give the player a collider so it doesn't fall through the floor!
    # The FirstPersonController does not have one by default.
    collider='capsule' 
)

# Function to handle input
def input(key):
    # Check if the pressed key is 'escape'
    if key == 'escape':
        quit()  # Quit the application

    # Check if the key is 'left mouse down'
    if key == 'left mouse down':
        # Now, we spawn our new FallingCube class
        new_cube = FallingCube(
            model='cube',
            texture='white_cube',
            collider='box', # The player can collide with this
            # Place it 2 units in front of the camera
            # We add a small vertical offset so it doesn't spawn inside the player
            position = player.position + camera.forward * 2 + Vec3(0, 0.5, 0)
        )

# Run the application
app.run()
