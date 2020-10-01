def solution(A):
    """
    A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
    Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
    The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
    In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
    :param A: non-empty array A of N integers
    :return: minimal difference
    """
    absolute = 2000
    left = A[0]
    right = sum(A[1:])
    tmp_absolute = calc_absolute(left, right)
    if tmp_absolute < absolute:
        absolute = tmp_absolute
    i = 1
    while i != len(A) - 1:
        left += A[i]
        right -= A[i]
        tmp_absolute = calc_absolute(left, right)
        if tmp_absolute < absolute:
            absolute = tmp_absolute
        i += 1
    return absolute


def calc_absolute(left, right):
    """
    Calculate absolute difference
    """
    abs = left - right
    if abs < 0:
        abs *= -1
    return abs


