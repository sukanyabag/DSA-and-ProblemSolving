'''
Problem statement- 
Given a number N find the number of ways to express N as a sum 
of 1,3 and 4.

ex1-
N=4, ways = 4 [{4}, {1,3},{3,1},{1,1,1,1}]

top-down approach-
def NumberFactor(N, dp): #step1
  if N in (0,1,2) return 1
  if N=3 return 2
  
  elif N in dp return dp[N] #step2

  else:
      rec1 = NumberFactor(N-1)
      rec2 = NumberFactor(N-3)
      rec3 = NumberFactor(N-4)

      dp[N] = rec1 + rec2 + rec3 #step3
      return dp[N] #step4

bottom-up approach-
def NumberFactor(N):
    tab = [1,1,1,2]
    for i in range(4,n+1):
        tab.append(tab[i-1]+tab[i-3]+tab[i-4])
    return tab[n]
      
'''
#top-down
def NumberFactor(n, tempDict):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        if n not in tempDict:
            subprob1 = NumberFactor(n-1, tempDict)
            subprob2 = NumberFactor(n-3, tempDict)
            subprob3 = NumberFactor(n-4, tempDict)
            tempDict[n] = subprob1 + subprob2 + subprob3
        return tempDict[n]

print(NumberFactor(5, {}))

#bottom-up (better)
def NumberFactor(n):
    temp_arr = [1,1,1,2]
    for i in range(4,n+1):
        temp_arr.append(temp_arr[i-1]+temp_arr[i-3]+temp_arr[i-4])
    return temp_arr[n]

print(NumberFactor(5))


    
