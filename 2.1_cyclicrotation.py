def solution(A, K):
    """
    Rotate an array to the right by a given number of steps.
    :param A: array A consisting of N integers
    :param K: integer within the range [0..100];
    :return:  the array A rotated K times.
    """
    length = len(A)
    if length == 0:
        return A
    mod_k = K % len(A)
    new = []
    new[0:mod_k] = A[length - mod_k:]
    new[mod_k+1:] = A[:length - mod_k]
    return new
