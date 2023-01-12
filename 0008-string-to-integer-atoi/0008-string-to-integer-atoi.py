class Solution:
    def myAtoi(self, s: str) -> int:
        
        max_int = 2**31 - 1
        min_int = -2**31
        output = 0
        itr = 0
        positive = 1
        lenth = len(s)
        digit_checker = set('0123456789')
        
        # ignore any leading whitespace
        while itr<lenth and s[itr] == ' ':
            itr += 1
            
        # Check if the next character '-' or '+'
        if itr<lenth and s[itr] == '-':
            positive = -1
            itr +=1
        elif itr<lenth and s[itr] == '+':
            positive = 1
            itr += 1
            
        # filter numbers
        while itr< lenth and s[itr] in digit_checker:
            # integer range 
            if max_int//10 < output or (max_int//10 == output and 7<int(s[itr])):
                return max_int if positive == 1 else min_int
            
            output = output*10 + int(s[itr])
            itr += 1
        
        return output * positive