""" Unit step sequence """
from numpy import arange, int16


def stepseq(n0, n1, n2):
    """ Generates x(n) = u(n-n0); n1 <= n <= n2
        -------------------------------------------
        (x, n) = stepseq(n0, n1, n2)
    """
    n = arange(n1,n2+1)
    x = (n0 <= n).astype(int16)
    return x, n