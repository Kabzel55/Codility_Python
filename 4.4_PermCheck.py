def solution(A):
    """
    Check whether array A is a permutation
    :param A: non-empty array A consisting of N integers is given.
                N is an integer within the range [1..100,000];
    :return: returns 1 if array A is a permutation and 0 if it is not.
    """
    if sum(range(1, len(set(A))+1)) - sum(A) == 0:
        return 1
    return 0