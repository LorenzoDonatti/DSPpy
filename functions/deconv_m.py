import numpy as np
from scipy.signal import deconvolve

def deconv_m(b, nb, a, na):
    """
    Modified deconvolution routine for noncausal sequences.
    
    Parameters:
        b (array): Numerator polynomial on support nb.
        nb (array): Support of b [nb1, nb2].
        a (array): Denominator polynomial on support na.
        na (array): Support of a [na1, na2].
        
    Returns:
        p (array): Polynomial part of support np.
        np (array): Support of p [np1, np2].
        r (array): Remainder part of support nr.
        nr (array): Support of r [nr1, nr2].
    """
    p, r = deconvolve(b, a)
    
    np1 = nb[0] - na[0]
    np2 = np1 + len(p) - 1
    n_p = np.arange(np1, np2 + 1)
    
    nr1 = nb[0]
    nr2 = nr1 + len(r) - 1
    nr = np.arange(nr1, nr2 + 1)
    
    return p, n_p, r, nr