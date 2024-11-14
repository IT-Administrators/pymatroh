"""
Pymatroh

A cross plattform matrix creation module for Python.

Usage:
    from pymatroh import matrix as imat
    im = imat.Matrix(2,2)
    im.create_int_matrix()

Return:
    [[100, 24], [90, 84]]

Usage:
    from pymatroh import matrix as fmat
    fm = fmat.Matrix(2,2)
    fm.create_float_matrix()

Return:
    [[0.3476066056691818, 82.64139933693019], [55.6682714565969, 37.442624968338635]]

Usage:
    from pymatroh import matrix as cmat
    im = imat.Matrix(2,1)
    cm.create_complex_matrix()

Return:
    [[(16.081037664553943+86.97288344375117j)], [(21.18506273716121+92.88016833034504j)]]

Usage:
    import pymatroh
    im = pymatroh.matrix.Matrix(1,1)
    im.create_int_matrix()

Return:
    [[53]]    

Author: IT-Administrators
License: MIT

"""

__all__ = ["Matrix"]