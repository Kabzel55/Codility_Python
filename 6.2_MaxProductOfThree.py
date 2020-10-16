def solution(A):
    """
    Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).
    :param A: non-empty array
    :return: maximal product of any triplet
    """
    A.sort(reverse=True)
    N = len(A)
    the_first_three = A[0] * A[1] * A[2]
    the_last_three = A[N-1] * A[N-2] * A[N-3]
    first_and_two_last = A[0] * A[N-1] * A[N-2]
    return max(the_first_three, the_last_three, first_and_two_last)

