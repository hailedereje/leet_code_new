class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        lst =[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    max = nums2[j]
                    for m in range(j+1,len(nums2)):
                        if nums2[m] > max:
                            max = nums2[m]
                    if nums2[j] == nums2[len(nums2)-1]:
                        lst.append(-1)
                    elif nums2[j] == max:
                            lst.append(-1)
                    for k in range(j+1,len(nums2)):
                       
                
                        if nums2[j] < nums2[k]:

                            lst.append(nums2[k])
                            break
                        
        return lst
