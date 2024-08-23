import numpy as np

def evenodd_to_complex_symmetry_modify(x,n):

    m1,m2 = np.min([-np.flip(n),n]), np.max([-np.flip(n),n])
    m = np.arange(m1,m2+1)

    x1 = np.zeros(len(m),dtype=np.complex128)
    n1 = np.arange(n[0]-m[0], len(n) + n[0]-m[0])
    x1[n1] = x
    x = x1

    xe = (x + np.conj(x[::-1])) / 2
    xo = (x - np.conj(x[::-1])) / 2
    return xe, xo, m