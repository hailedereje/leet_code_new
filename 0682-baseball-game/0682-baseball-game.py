class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lst=[]
        for i in operations:
            if i=="C":
                lst.pop()
            elif i=="D":
                lst.append(lst[-1]*2)
            elif i=="+":
                sm=lst[-2]+lst[-1]
                lst.append(sm)
            else:
                lst.append(int(i))
        print(lst)
        return sum(lst)