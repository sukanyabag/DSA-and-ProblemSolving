class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #init adj list premap for mapping courses with prereqs
        premap = {c:[] for c in range(numCourses)}
        
        #fill premap
        for crs,pre in prerequisites:
            premap[crs].append(pre)
            
        res = [] #init result as an empty list
        '''
        Note - A course has 3 possible states - 
        1. VISITED - course is added to res
        2. VISITING - course not added to res since cycle detected while visiting
        3. UNVISITED - course neither added to res nor to cycle
        '''
        visited, cycle = set(), set() #init visited and cycle sets
        
        #start dfs
        def dfs(crs):
            #base case 1 -if cycle detected for a course return false
            if crs in cycle:
                return False
            #base case 2 - if course already visited return true
            if crs in visited:
                return True
            
            #add to cycle if any new cycle detected for a course
            cycle.add(crs)
            
            #loop over all prerequisites in premap of a particular course
            for pre in premap[crs]:
                #if any prereq is not possible to achieve return false
                if not dfs(pre): return False
            #after loop executed make sure to remove that course from cycle
            #add it to visited
            #add it to result and then return true
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            
            return True
        
        #this is required in case we have unassociated graphs to carry out dfs manually on each
        for c in range(numCourses):
            if not dfs(c): return []
        return res
            
        
        
