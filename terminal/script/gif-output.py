'''
gif-output.py
Brownian-CA Infection Simulation's GIF output script
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
'''

import imageio

steps = 40
name = 'ca-simulation'

frames = []
for i in range(steps):
    frames.append(imageio.imread(f'./temp/step{i}.png'))
imageio.mimsave(f'./out/{steps}_{name}.gif', frames, 'GIF', duration = 0.1)