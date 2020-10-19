def solution(A):
    """
    Find an index of an array such that its value occurs at more than half of indices in the array.
    :param A: An array A consisting of N integers is given
    :return:  returns index of any element of array A in which the dominator of A occurs.
     The function should return −1 if array A does not have a dominator.
    """
    N = len(A)
    size = 0
    value = 0
    idx = -1
    for i in range(0, N):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
    candidate = -1
    if size > 0:
        candidate = value
    counter = 0
    for k in range(0, N):
        if A[k] == candidate:
            counter += 1
            idx = k
    if counter <= N // 2:
        idx = -1
    return idx
