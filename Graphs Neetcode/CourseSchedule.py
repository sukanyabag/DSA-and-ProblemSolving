class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        
        #append prereq to courses
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
            
        #visited set -> keeps track of all courses along dfs path
        visited = set()
        
        def dfs(crs):
            #base case 1 -> if cycle found in graph return false
            if crs in visited:
                return False
            #base case 2 -> can be completed, as no connected edges(pre) of this node(crs)
            if preMap[crs] == []:
                return True
            
            #if none of the above cases, add the crs to the visited set
            visited.add(crs)
            
            #check for pre of a crs in premap-> if a crs cannot be completed ret False
            for pre in preMap[crs]:
                if not dfs(pre): return False
                
            #if possible tho remove it's crs from visited meaning its done
            visited.remove(crs)
            
            #set that crs in premap to empty list
            preMap[crs] = []
            
            return True
        
        #for unassociated graphs like 1->2 , 3 -> 4 manually check for every crs,pre
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
        
