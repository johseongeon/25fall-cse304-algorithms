# name: 
# student id: 
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1

    # Complete the code here
    while low <= high and location == -1:
        mid = (low + high) // 2
        if (S[mid] == x):
            location = mid
        elif(x < S[mid]):
            high = mid-1
        else:
            low = mid+1

    return location