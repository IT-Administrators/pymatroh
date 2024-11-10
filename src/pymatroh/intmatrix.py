"""Create integer matrices."""

# Include necessary modules.
import random

class IntMatrix:
    """Create a matrix containing only integers."""

    def __init__(self, row: int, col: int, irange = 100):
        self.row = row
        self.col = col
        self.irange = irange

    def create_matrix(self):
        """Create a random integer matrix."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                childmatrix.append(random.randint(0,self.irange))
            matrix.append(childmatrix)
        return matrix
