class Solution(object):
    def pancakeSort(self,arr):
        list=[]
        l = len(arr)
        for j in range(l):
            maxx = max(arr[:l-j])
            maxindex=arr.index(maxx)+1
            arr[:maxindex] = reversed(arr[:maxindex])
            list.append(maxindex)
            
            arr[:l-j]=reversed(arr[:l-j])
            list.append(l-j)
        return list
