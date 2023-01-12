class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        st = ''
        res= []
        for i in range(len(s)):
            if s[i].isnumeric():
                st += s[i]
            else:
                if len(st)>0:
                    res.append(int(st))
                st =''
        if len(st)>0:
            res.append(int(st))
        for i in range(0,len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True