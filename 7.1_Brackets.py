def solution(S):
    """
    Determine whether a given string of parentheses (multiple types) is properly nested.
    :param S: string consisting of N characters
    :return: 1 if S is properly nested and 0 otherwise.
    """
    if len(S) % 2 != 0:
        return 0
    opened_bracks = ['(', '[', '{']
    closed_bracks = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for brack in S:
        if brack in opened_bracks:
            stack.append(brack)
        if len(stack) == 0:
            return 0
        if brack in closed_bracks.keys():
            if closed_bracks[brack] != stack.pop():
                return 0
    if len(stack) > 0:
        return 0
    return 1






a = "(("
print(solution(a))