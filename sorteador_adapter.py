import numpy as np

def definir_seed(nova_seed):
    np.random.seed(seed=nova_seed)

def sorteador():
    return np.random.randint(1, ((2**32) - 1))

class Sorteador:
    def __init__(self, seed):
        self.sorteador = np.random.RandomState(seed=seed)

    def sortear(self):
        return self.sorteador.randint(1, ((2**32) - 1))
