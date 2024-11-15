import numpy as np

def kl_d(P,Q):
    H = 0
    H_c = 0
    KL = 0
    for i, x in enumerate(P):
        if x > 0:
            H += -x*np.log2(x)
        if Q[i] > 0:
            H_c += -x*np.log2(Q[i])

    # H = -np.sum(P * np.log2(P + 1e-9)) 
    # H_c = -np.sum(P * np.log2(Q + 1e-9))
    
    KL = H_c - H

    return H, H_c, KL

if __name__== "__main__":
    P = np.array([.5,.5])
    Q = np.array([.6, .4])
    print(kl_d(P, Q))