class Solution:
    def nextGreaterElement(self, nums1, nums2):
        outputList = []
        for i in nums1:
            start = nums2.index(i)
            j = start+1
            while j < len(nums2):
                if nums2[j] > i:
                    outputList.append(nums2[j])
                    break
                #print(j)
                j+=1
            #print(j)
            if(j==len(nums2)):
                outputList.append(-1)
        
        return outputList