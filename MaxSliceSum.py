from sys import maxsize


def solution(A):
    """
        Find a maximum sum of a compact subsequence of array elements.

    """
    max_ending = -maxsize
    max_slice = -maxsize
    for number in A:
        max_ending = max(number, max_ending + number)
        max_slice = max(max_ending, max_slice)
    return max_slice
