def solution(A):
    """
    Compute the number of intersections in a sequence of discs.
    We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers,
     specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

    We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point
     (assuming that the discs contain their borders).
    :param A: array A describing N discs
    :return: returns the number of (unordered) pairs of intersecting discs.
     The function should return −1 if the number of intersecting pairs exceeds 10,000,000.
    """
    circles = []
    for center, radius in enumerate(A):
        circles.append([center - radius, 'Left'])
        circles.append([center + radius, 'Right'])
    circles.sort(key=lambda a: (a[0], a[1]))
    counter_interactions = 0
    open_circle = 0
    for point, side in circles:
        if side == 'Left':
            counter_interactions += open_circle
            open_circle += 1
        else:
            open_circle -= 1
    if counter_interactions > 10000000:
        return -1
    else:
        return counter_interactions
