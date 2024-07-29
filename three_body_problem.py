import numpy as np


class planet:
    def __init__(self, name, m, r0, v0):
        self.name = name
        self.a = np.zeros((len(t_points),3))
        self.v = np.zeros((len(t_points),3))
        self.r = np.zeros((len(t_points),3))
        self.m = m
        self.v[0] = v0
        self.r[0] = r0


def three_body_interaction(p1,p2,p3):
    r12 = p2.r - p1.r
    r23 = p3.r - p2.r
    r13 = p3.r - p1.r
    for i in range(0, len(t_points) - 1 ):
        r12_hat = r12[i] / np.linalg.norm(r12[i])
        r23_hat = r23[i] / np.linalg.norm(r13[i])
        r13_hat = r13[i] / np.linalg.norm(r23[i])

        #update particle 1s coordinate
        p1.a[i + 1] = r12_hat * G * p2.m / (np.linalg.norm(r12[i]) ** 2) + r13_hat * G * p3.m / (np.linalg.norm(r13[i]) ** 2)
        p1.v[i + 1] = p1.v[i] + p1.a[i] * dt
        p1.r[i + 1] = p1.r[i] + p1.v[i] * dt
        

        #update particle 2s coordinates
        p2.a[i + 1] =  -(r12_hat * G * p1.m / (np.linalg.norm(r12[i]) ** 2)) + r23_hat * G * p3.m / (np.linalg.norm(r23[i]) ** 2)
        p2.v[i + 1] = p2.v[i] + p2.a[i] * dt
        p2.r[i + 1] = p2.r[i] + p2.v[i] * dt

        #update particle 3s coordinates
        p3.a[i +1] =  - (r13_hat * G * p1.m / (np.linalg.norm(r13[i]) ** 2)) - (r23_hat * G * p2.m / (np.linalg.norm(r23[i]) ** 2))
        p3.v[i + 1] = p3.v[i] + p3.a[i] * dt
        p3.r[i + 1] = p3.r[i] + p3.v[i] * dt

        r12[i + 1] = p2.r[i + 1] - p1.r[i + 1]
        r23[i + 1] = p3.r[i + 1] - p2.r[i + 1]
        r13[i + 1] = p3.r[i + 1] - p1.r[i + 1]


        print(f"Progress: {i / len(t_points) * 100}%")
    
    np.save(f'planet_data/{p1.name}_trag', p1.r)
    np.save(f'planet_data/{p2.name}_trag', p2.r)
    np.save(f'planet_data/{p3.name}_trag', p3.r)
    print('Tragectories Calculated!')


G = 6.674e-11
t_0 = 0  # seconds
t_f = 10000  # seconds
t_points = np.linspace(t_0, t_f, 1000000)
dt = t_points[1] - t_points[0]
    
p1 = planet('Planet1',1.0e26, np.array([0,0,0]), np.array([1e4, 2e4, 3e4]))   
p2 = planet('Planet2',1.0e26, np.array([3e6,0,0]), np.array([0, 4e4, 0]))
p3 = planet('Planet3',1.0e26, np.array([-3e6,0,0]), np.array([0, -4e4, 0]))

three_body_interaction(p1,p2,p3)


