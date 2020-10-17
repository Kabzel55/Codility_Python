def solution(A):
    """
    Determine whether a given string of parentheses (single type) is properly nested.
    """
    opened_bracks = 0
    closed_bracks = 0
    for bracket in A:
        if bracket == "(":
            opened_bracks += 1
        else:
            closed_bracks += 1
        if closed_bracks > opened_bracks:
            return 0
    if closed_bracks != opened_bracks:
        return 0
    return 1
