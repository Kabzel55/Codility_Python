from sys import maxsize


def solution(A):
    """
    Given a log of stock prices compute the maximum possible earning.
    """
    max_profit = 0
    min_bought = maxsize

    for day in A:
        min_bought = min(min_bought, day)
        max_profit = max(max_profit, (day - min_bought))
    return max(max_profit, 0)

