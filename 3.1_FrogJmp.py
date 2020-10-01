from math import ceil


def solution(X, Y, D):
    """
    Count minimal number of jumps from position X to Y with jump D
    """
    return ceil((Y - X) / D)
