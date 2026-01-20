def fibo(n):
    if n<=1:
        return n
    if memo [n]:
        return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())
memo = [0] * (n+1)
print(fibo(n))