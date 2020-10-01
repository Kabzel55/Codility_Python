def solution(A):
    """
    Find the missing element in a given permutation.
    :param A:  An array A consisting of N different integers is given.
     The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
    :return: the value of the missing element.
    """
    if len(A) == 0:
        return 1
    return sum(range(1, len(A) + 2)) - sum(A)

