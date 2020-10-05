def solution(A, B, K):
    """
    Compute number of integers divisible by k in range [a..b].
    """
    i = 0
    if A % K == 0:
        i = 1
    return ((B // K) - (A // K) + i)