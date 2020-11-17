def create_peaks(A):
    N = len(A)
    peaks = ([True if A[i] > A[i - 1] and A[i] > A[i + 1]
              else False
              for i in range(1, N - 1)])
    peaks.insert(0, False)
    peaks.append(False)
    return peaks


def next_peak(A):
    N = len(A)
    peaks = create_peaks(A)
    my_next = [0] * N
    my_next[N - 1] = -1
    for i in range(N - 2, -1, -1):
        if peaks[i]:
            my_next[i] = i
        else:
            my_next[i] = my_next[i + 1]
    return my_next


def solution(A):
    N = len(A)
    my_next = next_peak(A)
    i = 1
    flags = 0
    while (i-1) * i <= N:
        curr_flags = 0
        pos_peak = 0
        while pos_peak < N and curr_flags < i:
            pos_peak = my_next[pos_peak]
            if pos_peak == -1:
                break
            curr_flags += 1
            pos_peak += i
        flags = max(flags, curr_flags)
        i += 1
    return flags

