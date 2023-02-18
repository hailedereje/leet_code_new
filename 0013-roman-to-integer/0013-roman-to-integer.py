class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
"I"       :      1,
"V"       :      5,
"X"       :      10,
"L"       :      50,
"C"        :     100,
"D"         :    500,
"M"          :   1000
        }
        romanList = []
        result = 0
        if len(s) == 1:
            return dic[s[0]]
        for i in s:
            if romanList:
                if dic[i] <= dic[romanList[-1]]:
                    result += dic[i]
                    romanList.append(i)
                    
                elif dic[i] > dic[romanList[-1]]:
                    result += dic[i]-2*dic[romanList[-1]]
                    romanList.append(i)
            else:
                romanList.append(i)
                result+=dic[i]
        return result
                    
                    
                    
        