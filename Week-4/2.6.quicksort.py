from typing import List

def partition(low: int, high: int, S: List[int]) -> int:
    pivotitem = S[low]
    j = low

    # Complete the code here
    for i in range(low + 1, high + 1):
        if S[i] < pivotitem:
            j += 1
            S[i], S[j] = S[j], S[i]
    S[low], S[j] = S[j], S[low]
    return j



def quicksort(low: int, high: int, S: List[int]) -> None:
    if low < high:
        # Complete the code here
        partition_index = partition(low, high, S)
        quicksort(low, partition_index - 1, S)
        quicksort(partition_index + 1, high, S)