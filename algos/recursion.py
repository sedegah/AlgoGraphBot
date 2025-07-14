def factorial_trace(n, depth=0):
    indent = \"  \" * depth
    if n == 0:
        return f\"{indent}factorial(0) = 1\"
    return f\"{indent}factorial({n}) = {n} * factorial({n-1})\\n\" + factorial_trace(n-1, depth+1)

def fibonacci_trace(n, depth=0):
    indent = \"  \" * depth
    if n <= 1:
        return f\"{indent}fibonacci({n}) = {n}\"
    return (
        f\"{indent}fibonacci({n}) = fibonacci({n-1}) + fibonacci({n-2})\\n\" +
        fibonacci_trace(n-1, depth+1) + \"\\n\" +
        fibonacci_trace(n-2, depth+1)
    )
