'''
Given an array of integers A of size N and an integer B.
College library has N bags,the ith book has A[i] number of pages.
You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum.
A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.
NOTE: Return -1 if a valid assignment is not possible.

Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return that minimum possible number

Constraints
1 <= N <= 10^5
1 <= A[i] <= 10^5

For Example
Input 1:
    A = [12, 34, 67, 90]
    B = 2
Output 1:
    113
Explanation 1:
    There are 2 number of students. Books can be distributed in following fashion : 
        1) [12] and [34, 67, 90]
        Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
        2) [12, 34] and [67, 90]
        Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
        3) [12, 34, 67] and [90]
        Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

        Of the 3 cases, Option 3 has the minimum pages = 113.
'''
class Solution:
	# @param pages : list of integers
	# @param students : integer
	# @return an integer
    def allocationPossible(self, barrier, students, pages)-> bool:
        currStudent = 1
        pagesAllocated = 0
        
        #edge-case => if students > size(pages) game over
        if(students > len(pages)):
            return False
            
        for i in range(len(pages)):
            #if pages > barrier we cannot allocate
            if pages[i] > barrier:
                return False
                
            #if pages allocated to a student plus pages[i] is greater than barrier, we allocate pages[i] to next student
            if pagesAllocated + pages[i] > barrier:
                currStudent += 1
                pagesAllocated = pages[i]
            #if barrier not crossed, keep on allocating pages[i] to the current student
            else:
                pagesAllocated += pages[i]
        
        #more students needed than provided, for allocating all pages - FAILURE
        if (currStudent > students):
            return False
            
        #all students have been successfully allocated pages
        # and maximum number of pages alloted to a student is minimum. - SUCCESS 
        else:
            return True
                
	def allocateBooks(self, pages, students):
        #lower bound of binary search
        low = min(pages)
        #upper bound of binary search
        high = sum(pages)
        #init result to -1 as of now
        ans = -1
        
        #begin binary search 
        while (low <= high):
            #set mid as barrier
            barrier = low + (high - low) // 2;
            
            #check if allocationPossible
            #if yes keep on shrinking towards left to make sure -> max number of pages alloted to a student is min
            if(self.allocationPossible(barrier,students,pages)):
                ans = barrier
                high = barrier - 1
            #if not, increase the lower bound
            else:
                low = barrier + 1
                
        return ans
        
