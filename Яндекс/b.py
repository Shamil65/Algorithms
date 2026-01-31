import sys
import math

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    k = int(next(it))
    y = [int(next(it)) for _ in range(n)]
    
    total_nodes = 2 * n - 1
    left = [0] * (total_nodes + 1)
    right = [0] * (total_nodes + 1)
    
    for i in range(n + 1, total_nodes + 1):
        l_val = int(next(it))
        r_val = int(next(it))
        left[i] = l_val
        right[i] = r_val
    
    sz = [0] * (total_nodes + 1)
    ones = [0] * (total_nodes + 1)
    
    for v in range(1, n + 1):
        sz[v] = 1
        ones[v] = y[v - 1]
    
    for v in range(total_nodes, n, -1):
        lv = left[v]
        rv = right[v]
        sz[v] = sz[lv] + sz[rv]
        ones[v] = ones[lv] + ones[rv]
    
    def entropy(p):
        if p == 0 or p == 1:
            return 0.0
        return -p * math.log(p) - (1 - p) * math.log(1 - p)
    
    INF = float('inf')
    dp = [None] * (total_nodes + 1) 
    
    for v in range(1, n + 1):
        dp[v] = [INF] * (min(sz[v], k) + 1) 
        dp[v][0] = INF  
        if 1 <= len(dp[v]) - 1:
            dp[v][1] = 0.0
    
    for v in range(total_nodes, n, -1):
        lv = left[v]
        rv = right[v]
        max_t = min(sz[v], k)
        dp[v] = [INF] * (max_t + 1)
        dp[v][0] = INF
        
        if max_t >= 1:
            p = ones[v] / sz[v]
            dp[v][1] = entropy(p)
        
        L_len = len(dp[lv]) - 1  
        R_len = len(dp[rv]) - 1  
        for t in range(2, max_t + 1):
            low = max(1, t - R_len)
            high = min(L_len, t - 1)
            for t1 in range(low, high + 1):
                t2 = t - t1
                if t2 < 1 or t2 > R_len:
                    continue
                candidate = dp[lv][t1] + dp[rv][t2]
                if candidate < dp[v][t]:
                    dp[v][t] = candidate
    
    root = total_nodes
    result = dp[root][k]
    print(f"{result:.10f}")

if __name__ == "__main__":
    solve()