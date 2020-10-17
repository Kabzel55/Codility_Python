def solution(A, B):
    """
    N voracious fish are moving along a river. Calculate how many fish are alive.
    given two non-empty arrays A and B consisting of N integers

    :return: returns the number of fish that will stay alive.
    """
    N = len(A)
    dead = 0
    stack = []

    for idx, fish in enumerate(A):
        if B[idx] == 1:
            stack.append(fish)
        else:
            while len(stack) > 0:
                dead += 1
                if fish < stack[-1]:
                    break
                else:
                    stack.pop()
    return N - dead
