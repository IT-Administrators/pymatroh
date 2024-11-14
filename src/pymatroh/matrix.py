"""Create random matrices."""

# Include necessary modules.
import random

class Matrix:
    """Create a matrix containing only integers."""

    def __init__(self, row: int, col: int, irange = 100, applyround = False):
        self.row = row
        self.col = col
        self.irange = irange
        self.applyround = applyround

    def create_int_matrix(self):
        """Create a random integer matrix."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                childmatrix.append(random.randint(0, self.irange))
            matrix.append(childmatrix)
        return matrix
    
    def create_float_matrix(self):
        """Create a random float matrix."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                if self.applyround == False:
                    childmatrix.append(random.uniform(0.0, self.irange))
                else:
                    childmatrix.append(round(random.uniform(0.0, self.irange), 3))
            matrix.append(childmatrix)
        return matrix
    
    def create_complex_matrix(self):
        """Create a random matrix with complex values."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                if self.applyround == False:
                    childmatrix.append(complex(random.uniform(0.0, self.irange), random.uniform(0.0, self.irange)))
                else:
                    childmatrix.append(complex(round(random.uniform(0.0, self.irange), 3), round(random.uniform(0.0, self.irange), 3)))
            matrix.append(childmatrix)
        return matrix
