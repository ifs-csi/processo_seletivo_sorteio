import numpy as np

class Sorteador:
    def __init__(self, seed):
        self.sorteador = np.random.RandomState(seed=seed)

    def sortear(self):
        return self.sorteador.randint(1, ((2**32) - 1))
