from typing import List

def merge(h: int, m: int, U: List[int], V: List[int], S: List[int]) -> None:
    assert sorted(U) == U
    assert sorted(V) == V
    
    i = j = k = 0
    # Complete the code here
    while i < h and j < m:
        if U[i] <= V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    # i, j 중 하나가 끝에 도달했을 때 남은 원소들을 복사
    while i < h:
        S[k] = U[i]
        i += 1
        k += 1
    while j < m:
        S[k] = V[j]
        j += 1
        k += 1

def mergesort(n: int, S: List[int]) -> None:
    h = n // 2
    m = n - h
    if n > 1:
        # Complete the code here
        U = S[:h]
        V = S[h:]
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)
