from typing import Dict, Tuple

def knapsack(n: int, W: int, DP: Dict[Tuple[int, int], int]) -> int:
    global w, p
    if n == 0 or W <= 0:
        DP[(n, W)] = 0
    else:
        # Complete the code here
        if (n, W) in DP:
            return DP[(n, W)]

        if w[n] > W:
            DP[(n, W)] = knapsack(n - 1, W, DP)
        else:
            include = p[n] + knapsack(n - 1, W - w[n], DP)
            exclude = knapsack(n - 1, W, DP)
            DP[(n, W)] = max(include, exclude)

        pass

    return DP[(n, W)]