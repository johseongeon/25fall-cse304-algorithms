from typing import List

n: int
W: int
w: List[int]
include: List[int]

def promising(i: int, weight: int, total: int) -> bool:
    global n, W, w, include
    # Complete the code here
    can_reach_W = (weight + total >= W)
    
    if i < n:
        can_include_next = (weight == W) or (weight + w[i+1] <= W)
        return can_reach_W and can_include_next
    
    return weight == W

def sumofsubsets(i: int, weight: int, total: int) -> None:
    global n, W, w, include
    if promising(i, weight, total):
        if weight == W:
            print("found:", include[1:])
        else:
            # Complete the code here
            j = i + 1
            include[j] = 1
            sumofsubsets(j, weight + w[j], total - w[j])
            include[j] = 0
            if weight + total - w[j] >= W:
                sumofsubsets(j, weight, total - w[j])