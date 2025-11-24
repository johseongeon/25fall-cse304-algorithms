from typing import List

class Node:
    def __init__(self, level, weight, profit):
        self.level = level
        self.weight = weight
        self.profit = profit

def boundof(u: Node, n: int, W: float, w: List[float], p: List[float]) -> float:
    if u.weight >= W:
        return 0
    else:
        # Complete the code here
        result = u.profit
        j = u.level + 1
        totweight = u.weight
        while j <= n and totweight + w[j] <= W:
            totweight += w[j]
            result += p[j]
            j += 1
        k = j
        if k <= n:
            result += (W - totweight) * p[k] / w[k]
        return result

def knapsack2(n: int, W: float, w: List[float], p: List[float]) -> float:
    count = 0
    queue = [] # Initialize Queue
    v = Node(0, 0, 0)
    bound = boundof(v, n, W, w, p)
    maxprofit = 0
    queue.append(v)
    count+=1
    while len(queue) != 0:
        # Complete the code here
        v = queue.pop(0)
        if v.level < n:
            # 다음 아이템 추가
            u = Node(v.level + 1, v.weight + w[v.level + 1], v.profit + p[v.level + 1])
            if u.weight <= W and u.profit > maxprofit:
                maxprofit = u.profit
            bound = boundof(u, n, W, w, p)
            if bound > maxprofit:
                queue.append(u)
                count += 1
            
            u = Node(v.level + 1, v.weight, v.profit)
            bound = boundof(u, n, W, w, p)
            if bound > maxprofit:
                queue.append(u)
                count += 1
    return maxprofit
