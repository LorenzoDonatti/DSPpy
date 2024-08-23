import numpy as np

def dtft(x,n,w):
    """
    Computes Discrete-time Fourier Transform.

    Parameters:
        x (array): Finite duration sequence over n.
        n (array): Sample position row vector.
        w (array): Frequency row vector, w = k*pi/M, k = 0:M.
S
    Returns:
        X (array): DTFT values computeSd at w frequencies.
    """
    X = x @ np.exp(-1j * n.reshape(-1,1) * w)
    return X
