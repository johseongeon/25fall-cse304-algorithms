from typing import List

def insertionsort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(1, n):
        key = S[i]
        j = i - 1
        # Move elements of S[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and S[j] > key:
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = key
    return