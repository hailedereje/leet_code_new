class Solution:
    def calculate(self,s: str) -> int:
        def cal(n1,n2,o):
            if o == "+":
                return n1+n2
            elif o == "-":
                return n1-n2
            elif o == "*":
                return n1*n2
            elif o == "/":
                return int(n1/n2)
        def convert(s):
            collector = []
            st = 0
            for i,j in enumerate(s):
                if j in "+-*/":
                    collector.append(s[st:i])
                    collector.append(s[i])
                    st = i+1
            collector.append(s[st:])
            return collector

        s = convert(s)
        stack2 = []
        for j,i in enumerate(s):
            if i in "*/":
                stack2[-1] = cal(int(stack2[-1]),int(s[j+1]),i)
                s.pop(j+1)   
            elif i in "+-":
                stack2.append(i)
            else:
                stack2.append(int(i))
        sum = stack2[0]
        i = 1
        while(i<len(stack2)):
            sum = cal(sum,stack2[i+1],stack2[i])
            i+=2
        return int(sum)