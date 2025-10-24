a, b, c, v0, v1, v2 = map(int, input().split())

t1 = a/v0 + c/v1 + b/v2
t2 = b/v0 + c/v1 + a/v2
t3 = a/v0 + c/v1 + c/v2 + a/v2
t4 = b/v0 + c/v1 + c/v2 + b/v2
t5 = a/v0 + a/v1 + b/v0 + b/v1
t6 = b/v0 + b/v1 + a/v0 + a/v1

print(min(t1, t2, t3, t4, t5, t6))
