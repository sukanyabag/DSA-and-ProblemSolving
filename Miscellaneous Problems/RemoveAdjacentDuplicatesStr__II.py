'''
Save the character char and its count to the stack.
If the next character char is same as the last one, increment the count.
Otherwise push a pair (char, 1) into the stack.
use a dummy element ('$', 0) to avoid empty stack.

Time O(N) for one pass
Space O(N)

'''

    def removeDuplicates(self, s, k):
        stack = [['$', 0]]
        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(char * k for char, k in stack)
