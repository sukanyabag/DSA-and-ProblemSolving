'''
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward)
for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:
StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.
 
Example 1:
Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal to today's price.
stockSpanner.next(85);  // return 6
 
Constraints:
1 <= price <= 105
At most 104 calls will be made to next.
'''

'''
SOLUTION - MONOTONIC STACK 

Time complexity of each call to next: O(1)

Even though there is a while loop in next, that while loop can only run n times total across the entire algorithm.
Each element can only be popped off the stack once, and there are up to n elements.

This is called amortized analysis - if you average out the time it takes for next to run across nnn calls, 
it works out to be O(1). If one call to next takes a long time because the while loop runs many times, then the other calls to
next won't take as long because their while loops can't run as long.

Space complexity: O(n)
In the worst case scenario for space (when all the stock prices are decreasing), the while loop will never run, which means the stack grows to a size of n.
'''

class StockSpanner:
    def __init__(self):
        self.stack = [] # pair: (price, span)
        
    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop() 
        self.stack.append((price,span))

        return span   
