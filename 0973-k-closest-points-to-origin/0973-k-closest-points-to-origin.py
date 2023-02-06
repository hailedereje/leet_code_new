class Solution:
     def kClosest(self, points: list[list[int]], k: int):
            val = [[i[0]**2 + i[1]**2,i] for i in (points)]
            val.sort()
            sett = []
            while(len(sett)<k):
                sett.append(val.pop(0)[1])

            return sett
                
                
                
                
                
                
                
                