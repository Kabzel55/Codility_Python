def solution(S, P, Q):
    """
        Find the minimal nucleotide from a range of sequence DNA.
    """
    result = []
    impact = dict(A=1, C=2, G=3, T=4)
    for i in range(0, len(P)):
        for imp in impact:
            if imp in S[P[i]:Q[i]+1]:
                result.append(impact[imp])
                break
    return result



