import numpy as np

def evenodd(x,n):

    m1,m2 = np.min([-np.flip(n),n]), np.max([-np.flip(n),n])
    m = np.arange(m1,m2+1)

    x1 = np.zeros(len(m))
    n1 = np.arange(n[0]-m[0], len(n) + n[0]-m[0])
    x1[n1] = x
    x = x1

    even = (x + x[::-1]) / 2
    odd = (x - x[::-1]) / 2
    
    return even, odd, m