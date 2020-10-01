def solution(N):
    '''
    Find longest sequence of zeros in binary representation of an integer.
    :param N: Integer
    :return: a count of the longest sequence of zeros in the binary representation of the integer
    '''

    N = bin(N)[2:].strip('0').split('1')
    return max(len(i) for i in N)