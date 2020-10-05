def solution(A):
    """
    Find the smallest positive integer that does not occur in a given sequence
    :param A: A non-empty array A of N integers is given
    :return: returns the smallest positive integer (greater than 0) that does not occur in A.
    """
    A = sort_01(A)
    if len(A) == 0:
        return 1
    A = set(A)
    for number in range(1, len(A) + 1):
        if number not in A:
            return number
    return number + 1


def sort_01(A):
    """

    :param A:  A non-empty array A of N integers is given
    :return:  array A with only positive numbers
    """
    pointer = 0
    for key, value in enumerate(A):
        if value < 0:
            tmp = A[pointer]
            A[pointer] = A[key]
            A[key] = tmp
            pointer += 1
    return A[pointer:]
