from typing import List

# Global variable type declarations
n: int
W: float
w: List[float]
p: List[float]
maxprofit: float
bestset: List[bool]
include: List[bool]

def promising(i: int, weight: float, profit: float) -> bool:
    global n, W, w, p, maxprofit
    # Complete the code here
    if weight >= W:
        return False
    bound: float = profit
    j: int = i + 1
    totalweight: float = weight
    while j <= n and totalweight + w[j] <= W:
        totalweight += w[j]
        bound += p[j]
        j += 1
    if j <= n:
        bound += (W - totalweight) * p[j] / w[j]

    return bound > maxprofit

def knapsack(i: int, weight: float, profit: float) -> None:
    global n, W, w, p, bestset, include, maxprofit
    if weight <= W and profit > maxprofit:
        # Complete the code here
        maxprofit = profit
        bestset = include[:]
    if promising(i, weight, profit):
        # Complete the code here
        include[i + 1] = True
        knapsack(i + 1, weight + w[i + 1], profit + p[i + 1])
        include[i + 1] = False
        knapsack(i + 1, weight, profit)
