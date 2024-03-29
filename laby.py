import numpy as np
from random import randint

def create_lab(lab):
    M = np.full([lab['size'], lab['size']], ' ')
    for i in range(lab['size']):
        M[0, i] = 'X'
        M[i, 0] = 'X'
        M[-1, i] = 'X'
        M[i, -1] = 'X'
    for wall in lab['walls']:
        M[wall[0], wall[1]] = 'X'
    M[1, 0] = ' '
    M[-2, -1] = ' '
    return M

import random
random.seed()
def empty_lab(size):
    return { 'size': size, 'walls': set() }


def lab_alea(size, nbWalls):
    lab = empty_lab(size)
    for i in range(nbWalls):
        lab['walls'].add((randint(0, size-1), randint(0, size-1)))
    return lab

