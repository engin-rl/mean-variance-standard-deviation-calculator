import numpy as np


def calculate(self):
    if len(self) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(self).reshape(3, 3)

        calculations = {
            "mean": [
                np.mean(matrix, axis=0).tolist(),
                np.mean(matrix, axis=1).tolist(),
                np.mean(matrix.flatten()).tolist(),
            ],
            "variance": [
                np.var(matrix, axis=0).tolist(),
                np.var(matrix, axis=1).tolist(),
                np.var(matrix.flatten()).tolist(),
            ],
            "standard deviation": [
                np.std(matrix, axis=0).tolist(),
                np.std(matrix, axis=1).tolist(),
                np.std(matrix.flatten()).tolist(),
            ],
            "max": [
                np.max(matrix, axis=0).tolist(),
                np.max(matrix, axis=1).tolist(),
                np.max(matrix.flatten()).tolist(),
            ],
            "min": [
                np.min(matrix, axis=0).tolist(),
                np.min(matrix, axis=1).tolist(),
                np.min(matrix.flatten()).tolist(),
            ],
            "sum": [
                np.sum(matrix, axis=0).tolist(),
                np.sum(matrix, axis=1).tolist(),
                np.sum(matrix.flatten()).tolist(),
            ],
        }

    return calculations
