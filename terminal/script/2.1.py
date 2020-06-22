import numpy as np
from matplotlib import pyplot as plt
import random

size = 10
foods = np.random.rand(size, size)*5
inserts = np.random.rand(size, size)
for i in range(size):
    for j in range(size):
        if inserts[i, j] < .9:
            inserts[i, j] = 0


def consumes():
    for i in range(size):
        for j in range(size):
            foods[i, j] = 0 if inserts[i, j] >= foods[i,
                                                      j] else foods[i, j] - inserts[i, j]


def moves():
    for i in range(size):
        for j in range(size):
            move(i, j)


directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def food_around(i,j):
    for di,dj in directions:
        if i+di in (-1,size) or j+dj in (-1,size):
            yield 0
        else:
            yield foods[i+di,j+dj]

def max_food_loc(i,j):
    food_around_list = list(food_around(i,j))
    food_around_indice = np.argmax(food_around_list)
    return directions[food_around_indice] 

def move(i,j):
    if foods[i,j] == 0: 
        di,dj = max_food_loc(i,j)
        inserts[i+di,j+dj] += inserts[i,j] 
        inserts[i,j] = 0


fig = plt.figure()
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)
plt.ion()
for i in range(50):
    plt.cla()
    ax0.imshow(inserts, cmap='Oranges')
    ax1.imshow(foods, cmap='Greens')
    consumes()
    moves()
    plt.pause(.2)
    plt.savefig(r'./temp/step{}.png'.format(i))
plt.ioff()
plt.show()
