# Recursion Tracing

def factorial_steps(n):
    steps = []

    def helper(x):
        if x == 0 or x == 1:
            steps.append(f"factorial({x}) = 1 (base case)")
            return 1
        steps.append(f"factorial({x}) = {x} * factorial({x - 1})")
        return x * helper(x - 1)

    result = helper(n)
    steps.append(f"Result: {result}")
    return "\n".join(steps)


def fibonacci_steps(n):
    steps = []

    memo = {}

    def helper(x):
        if x in memo:
            return memo[x]
        if x == 0:
            steps.append(f"fib(0) = 0 (base case)")
            memo[0] = 0
            return 0
        if x == 1:
            steps.append(f"fib(1) = 1 (base case)")
            memo[1] = 1
            return 1
        steps.append(f"fib({x}) = fib({x - 1}) + fib({x - 2})")
        memo[x] = helper(x - 1) + helper(x - 2)
        return memo[x]

    result = helper(n)
    steps.append(f"Result: {result}")
    return "\n".join(steps)
