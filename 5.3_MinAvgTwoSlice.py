def solution(A):
    """
    Find the minimal average of any slice containing at least two elements.
    :param A: each element of array A is an integer within the range [−10,000..10,000].
    :return: the smallest starting position of such a slice.
    """
    i = 0
    min_avg = 10000
    index = 0
    while i < len(A) - 2:
        tmp_avg2 = (A[i] + A[i+1]) / 2
        tmp_avg3 = (A[i] + A[i+1] + A[i+2]) / 3
        if tmp_avg2 < min_avg:
            min_avg = tmp_avg2
            index = i
        if tmp_avg3 < min_avg:
            min_avg = tmp_avg3
            index = i
        i += 1
    tmp_avg2 = (A[i] + A[i + 1]) / 2
    if tmp_avg2 < min_avg:
        index = i
    return index
