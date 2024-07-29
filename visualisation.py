import numpy as np
from vpython import sphere, vector, rate, canvas, color, vec, label

# Load positions from the saved numpy arrays

class planet:
    def __init__(self, name, radius, color):
        self.name = name
        self.r = np.load(f'planet_data/{name}_trag.npy')
        self.radius = radius
        self.color = color
        self.x = self.r[:, 0]
        self.y = self.r[:, 1]
        self.z = self.r[:, 2]
    
    def load_data(self):
        self.planet = sphere(pos=vector(self.x[0], self.y[0], self.z[0]), radius=self.radius , color=self.color, make_trail=True)
        self.label = label(pos=vector(self.x[0], self.y[0], self.z[0]), text=self.name, xoffset=20, yoffset=50, make_trail=False)
    
    def update_pos(self,index):
        self.planet.pos = vector(self.x[index], self.y[index], self.z[index])
        self.label.pos = vector(self.x[index], self.y[index], self.z[index])

# Create a VPython canvas
scene = canvas(title='Planetary Motion',
               width=1200, height=800,
               center=vector(0, 0, 0),
               background=color.black)

# Create sphere objects for the two planets
p1 = planet('Planet1',1e3, color.yellow)
p2 = planet('Planet2',1e3, color.blue)
p3 = planet('Planet3',1e3, color.white)


p1.load_data()
p2.load_data()
p3.load_data()

# Animation loop
for i in range(0,len(p3.x)):
    rate(10000)  # Adjust the rate to control the speed of the animation
    p1.update_pos(i)
    p2.update_pos(i)
    p3.update_pos(i)

