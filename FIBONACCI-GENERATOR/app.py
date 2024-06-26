def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    return series

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms (iterative): {fibonacci_iterative(n)}")

def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    def recur_fib(m):
        if m <= 1:
            return m
        else:
            return recur_fib(m-1) + recur_fib(m-2)
    
    series = [recur_fib(i) for i in range(n)]
    return series

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms (recursive): {fibonacci_recursive(n)}")

def fibonacci_memoized(n, memo=None):
    if memo is None:
        memo = {0: 0, 1: 1}
    
    if n in memo:
        return memo[n]
    
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Generate the series using the memoized function
def generate_fibonacci_series_memoized(n):
    return [fibonacci_memoized(i) for i in range(n)]

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms (memoized recursive): {generate_fibonacci_series_memoized(n)}")
