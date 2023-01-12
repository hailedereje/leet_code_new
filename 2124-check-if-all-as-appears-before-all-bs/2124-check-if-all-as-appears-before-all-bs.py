class Solution:
    def checkString(self, s: str) -> bool:
        c=s[0]
        if s[0]=='b' and 'a'  in s:
            return False
        n=len(s)
        for i in range(n):
            if c==s[i]:
                continue
            elif c in s[i+1:]:
                return False
        return True