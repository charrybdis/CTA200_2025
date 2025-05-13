def complex_iterate(R_c, I_c, max_iter=20, tol=1e6):
    '''Iterates over the function z_{n+1} = z^2 + c, where c is a constant
    
    Parameters: 
    R_c --- Real component of the constant c
    I_c --- Imaginary component of the constant c 
    max_iter ---- Maximum number of iterations
    tol --- Maximum difference between successive iterations
    
    Returns: 
    i --- Iteration number where the difference between successive iterations exceeds tol 
    None --- Returns None if the difference between iterations does not exceed tol 
    '''
    import numpy as np
    import cmath
    
    z = 0
    i = 0
    iteration_arr = np.empty(max_iter, dtype=np.complex_)
    c = complex(R_c, I_c)

    while i < max_iter:
        znew = (z ** 2) + c
        diff = abs(znew - z)
         
        if diff > tol: 
            return i 
        else:
            z = znew
            i += 1
    return None
