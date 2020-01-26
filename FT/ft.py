import numpy as np

class FT(object):
    def __init__(self):
        pass
    
    def ft(self, x, n_length=0):
         
        output = []

        if n_length==0:
            n_length = x.shape[0]
        
        for t in range(n_length):

            omega = 0
            for n in range(x.shape[0]):
                omega += x[n] * np.exp(-1j*((2.0*np.pi*t*n)/n_length))
            output.append(omega)
    
        return np.array(output)
    

    def ift(self, x, n_length=0):
        
        output = []

        if n_length==0:
            n_length = x.shape[0]

        for t in range(n_length):

            omega = 0
            for n in range(x.shape[0]):
                omega += x[n] * np.exp(1j*((2.0*np.pi*t*n)/n_length))
            output.append(omega/x.shape[0])
    
        return np.array(output)