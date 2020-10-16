def solution(A):
    """
        Count the number of passing cars on the road.

         A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

        Array A contains only 0s and/or 1s:

        0 represents a car traveling east,
        1 represents a car traveling west.


    :param A:   non-empty array
    :return:    the number of pairs of passing cars.
                The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
    """
    counter_east = 0
    passing_cars = 0
    for car in A:
        if car == 0:
            counter_east += 1
        else:
            passing_cars = passing_cars + counter_east
    if passing_cars > 1000000000:
        return -1
    return passing_cars
