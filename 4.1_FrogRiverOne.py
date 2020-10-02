def solution(X, A):
    """
    Find the earliest time when a frog can jump to the other side of a river.
    """
    leaves = {}
    for i in range(0, len(A)):
        leaves[A[i]] = 1
        if len(leaves) == X:
            return i
    return -1