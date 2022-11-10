'''
Keep a res as a characters stack.
Iterate characters of S one by one.

If the next character is same as the last character in res,
pop the last character from res.
In this way, we remove a pair of adjacent duplicates characters.

If the next character is different,
we append it to the end of res.

Time O(N) for one pass
Space O(N) for output
'''

    def removeDuplicates(self, S):
        res = []
        for char in S:
            if res and res[-1] == char:
                res.pop()
            else:
                res.append(char)
        return "".join(res)
