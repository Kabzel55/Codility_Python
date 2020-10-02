def solution(N, A):
    """
    Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
    You are given N counters, initially set to 0, and you have two possible operations on them:

    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents consecutive operations:

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    """
    B = [0] * (N + 1)
    base = 0
    max_counter = 0
    for i in A:
        if i <= N:
            if B[i] < base:
                B[i] = base
            B[i] += 1
            if B[i] > max_counter:
                max_counter = B[i]
        else:
          base = max_counter
    for key, value in enumerate(B):
        if value < base:
            B[key] = base
    return B[1:]
