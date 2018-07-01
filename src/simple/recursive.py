import numpy as np

def probabilityRR(T, M):
    """An implementation of the recursive win probability formula found in the my paper"""
    if M == 0:
        return 0
    elif M > (T - M):
        return 1
    else:
        term1 = ((T-M)/T)*probabilityRR(T-2, M)
        term2 = (M/T)*probabilityRR(T-2, M-1)
        return (term1 + term2)