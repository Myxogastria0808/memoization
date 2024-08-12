memo = [None]*101
memo[0] = 1
memo[1] = 1

def fib(num = 3):
    if memo[num] != None:
        return memo[num]
    else:
        memo[num] = fib(num-1)+fib(num-2)
        return memo[num]

print(fib(5))
print(memo)