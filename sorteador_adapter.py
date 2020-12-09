import numpy as np

def definir_seed(nova_seed):
    np.random.seed(seed=nova_seed)

def sorteador():
    return np.random.nextint(1, ((2**32) - 1))
