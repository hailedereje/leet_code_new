class Solution:
     def kClosest(self, points: list[list[int]], k: int):
            initial = [] 
            selected = []

            for i in points:
                heappush(initial,[i[0]**2 + i[1]**2,i])
            while len(selected) < k:
                current = heappop(initial)
                selected.append(current[1])

            return selected
                
                
                
                
                
                
                
                