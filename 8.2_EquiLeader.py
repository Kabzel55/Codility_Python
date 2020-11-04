def solution(A):
    """
    Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and
     A[S + 1], A[S + 2], ..., A[N - 1] are the same.
    :param A: A consisting of N integers [−1,000,000,000..1,000,000,000]
    :return:  the number of equi leaders (int)
    """

    from collections import Counter

    N = len(A)
    counter = Counter(A)
    leader, counter_leader = counter.most_common(1)[0]
    equi_leaders = 0

    if counter_leader > N // 2:
        left_size = 0
        left_counter_leader = 0
        for number in A:
            N -= 1
            left_size += 1

            if number == leader:
                left_counter_leader += 1
                counter_leader -= 1

            if left_counter_leader > left_size // 2 and counter_leader > N // 2:
                equi_leaders += 1
        return equi_leaders
    else:
        return 0



