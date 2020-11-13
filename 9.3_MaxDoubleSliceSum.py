def solution(A):
    """
    Find the maximal sum of any double slice.
    """
    left, now, total = 0, 0, 0
    N = len(A)
    for number in range(3, N):
        left = max(0, A[number-2] + left)
        now = max(left, A[number-1] + now)
        total = max(now, total)
    return total


