'''
top-down memoization-
solve the bigger problem by recursively finding the solution
to smaller subproblems, we cache its result so that we do not end
up solving it repeatedly if it's called multiple times.
This technique of storing the results of already solved subproblems 
is called Memoization.

fibonacci with memoizn-
algo-
Fibonacci(n): #time- O(n)
 if n<1 return error message
 if n=1 return 0
 if n=2 return 1
 if not n in memo:
     memo[n] = Fibonacci(n-1,memo) + Fibonacci(n-2, memo)
 return memo(n)
'''
def FibMemo(n, memo):
    if n==1:
        return 0
    if n==2:
        return 1
    if not n in memo:
        memo[n] = FibMemo(n-1, memo) + FibMemo(n-2, memo)
    return memo[n]

myDict = {}
print(FibMemo(6, myDict))
