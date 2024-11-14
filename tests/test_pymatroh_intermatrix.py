"""Testing the module with the python internal unittest module."""

import unittest

from addimportdir import importdir,removedir

# Import Matrix class from pymatroh
from pymatroh import matrix as imat

importdir()

test_matrices_quad = [(1,1), (2,2), (3,3), (4,4)] 
test_matrices_non_quad = [(1,2),(2,3),(1,4)]
testcases_length_quad_mat = [1, 2, 3, 4]
testcases_length_non_quad_mat = [1,2,1]

class TestPrerequistes(unittest.TestCase):
    def setUp(self):
        self.quad_mat = test_matrices_quad
        self.quad_mat_len = testcases_length_quad_mat
        self.non_quad_mat = test_matrices_non_quad
        self.non_quad_mat_len = testcases_length_non_quad_mat

    def test_equal_list_length(self):
        
        self.assertEqual(len(self.quad_mat), len(self.quad_mat_len))

    def test_non_equal_list_length(self):
        self.assertEqual(len(self.non_quad_mat), len(self.non_quad_mat_len))

class TestPymatrohMatrix(unittest.TestCase):
    """Test Monogram class of pyngramroh module."""

    def setUp(self):
        self.quad_mat = test_matrices_quad
        self.quad_mat_len = testcases_length_quad_mat
        self.non_quad_mat = test_matrices_non_quad
        self.non_quad_mat_len = testcases_length_non_quad_mat

    def test_mat_length_quad_mat(self):
        for ltest in range(len(self.quad_mat_len)):
            im = imat.Matrix(self.quad_mat[ltest][0],self.quad_mat[ltest][1])
            self.assertEqual(len(im.create_int_matrix()),self.quad_mat_len[ltest])
            self.assertEqual(len(im.create_float_matrix()),self.quad_mat_len[ltest])
            self.assertEqual(len(im.create_complex_matrix()),self.quad_mat_len[ltest])

    def test_mat_length_non_quad_mat(self):
        for ltest in range(len(self.non_quad_mat_len)):
            im = imat.Matrix(self.non_quad_mat[ltest][0],self.non_quad_mat[ltest][1])
            self.assertEqual(len(im.create_int_matrix()),self.non_quad_mat_len[ltest])
            self.assertEqual(len(im.create_float_matrix()),self.non_quad_mat_len[ltest])
            self.assertEqual(len(im.create_complex_matrix()),self.non_quad_mat_len[ltest])

if __name__ == '__main__':
    # Verbose unittests.
    unittest.main(verbosity=2)
    removedir()