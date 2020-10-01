def solution(A):
    """
    Find value that occurs in odd number of elements.
    :param A: A non-empty array A consisting of N integers is given.
    :return:  returns the value of the unpaired element.
    """
    dic_elems = {}
    for number in A:
        if number in dic_elems.keys():
            dic_elems[number] += 1
        else:
            dic_elems[number] = 1
    for key in dic_elems:
        if dic_elems[key] % 2 != 0:
            return key


