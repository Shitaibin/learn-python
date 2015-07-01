import numpy as np

def arandom(nsteps):
    draw = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draw > 0, 1, -1)
    walk = np.cumsum(steps)
    return walk

def nrandom(nwalks, nsteps):
    draw = np.random.randint(0, 2, size=(nwalks, nsteps))
    steps = np.where(draw > 0, 1, -1)
    walks = np.cumsum(steps, 1)
    return walks


