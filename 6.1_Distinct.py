def solution(A):
    """
    Compute number of distinct values in an array.
    :param A:  array A consisting of X integers
    :return:  the number of distinct values in array A.
    """
    counter = 1
    N = len(A)
    if N == 0:
        return 0
    A.sort()
    for i in range(1, N):
        if A[i] != A[i-1]:
            counter += 1
    return counter
