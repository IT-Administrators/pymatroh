"""Create random matrices."""

# Include necessary modules.
import random

class Matrix:
    """Create a matrix containing only integers."""

    def __init__(self, row: int, col: int, irange = 100):
        self.row = row
        self.col = col
        self.irange = irange

    def create_int_matrix(self):
        """Create a random integer matrix."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                childmatrix.append(random.randint(0,self.irange))
            matrix.append(childmatrix)
        return matrix
    
    def create_float_matrix(self):
        """Create a random float matrix."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                childmatrix.append(random.uniform(0.0,self.irange))
            matrix.append(childmatrix)
        return matrix
    
    def create_complex_matrix(self):
        """Create a random matrix with complex values."""

        matrix = []
        for i in range(self.row):
            childmatrix = []
            for j in range(self.col):
                childmatrix.append(complex(random.uniform(0.0,self.irange),random.uniform(0.0,self.irange)))
            matrix.append(childmatrix)
        return matrix
