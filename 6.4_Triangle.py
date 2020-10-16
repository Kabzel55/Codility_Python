def is_triangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        return 1


def solution(A):
    """
    Determine whether a triangle can be built from a given set of edges.

    :param A: array
    :return: returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
    """
    A.sort()
    N = len(A)
    for x in range(2, N):
        if is_triangle(A[x], A[x-1], A[x-2]) == 1:
            return 1
    return 0
