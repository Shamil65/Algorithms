# #==== Классика ====
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# print(fib(6))

# #==== Динамическая версия с кэшированием ====
def db_fib(n, db):
    if dp[n] == -1:
        return db_fib(n-1, db) + db_fib(n-2, db)
    return dp[n]

n = int(input())
dp = [-1] * (n+1)
dp[0] = dp[1] = 1
print(db_fib(n, dp))


#=== Фибоначи без рекурсии (я в шоке)
n = int(input())
dp = [0]*(n+1)
dp[0] = dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[i])


