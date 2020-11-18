def solution(N):
    """
    Find the minimal perimeter of any rectangle whose area equals N.
    """
    i = 1
    A = 1
    while i * i <= N:
        if N % i == 0:
            A = i
        i += 1
    # prime
    if A == 1:
        return N * 2 + 2
    # square
    if A * A == N:
        return 2 * (A + A)
    B = A+1
    while B <= N:
        if N % B == 0:
            return 2*(A+B)
        B += 1
    return 0
