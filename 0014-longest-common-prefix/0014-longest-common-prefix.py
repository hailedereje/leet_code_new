class Solution:
         
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strsVal = strs[0]
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs)):
            for j in range(min(len(strsVal),len(strs[i]))):
                if strsVal[j] != strs[i][j]:
                    break    
                prefix +=strs[i][j]
                
            strsVal = prefix 
            prefix = ""
        return strsVal
    
        
        
            

                    
                           