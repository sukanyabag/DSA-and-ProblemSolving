'''
Bottom-up with tabulation-
Tabulation is the opposite of topdown approach and avoids 
recursion. In this approach, we solve the problem bottom-up 
by solving the relted subproblems first. This is done
by filling a table. Based on the results in the table, the solution
to the top/original problem is then computed.

fibonacci with memoizn-
algo- #time - O(n), space-O(n)
def fibonaccTab(n):
    tab = [0,1]
    for i in range(2, n+1):
        tab.append(tab[i-1] + tab[i-2])
    return tab[n-1]
'''

def fibonacciTab(n):
    tab = [0,1]
    for i in range(2,n+1):
        tab.append(tab[i-1] + tab[i-2])
    return tab[n-1]

print(fibonacciTab(6))