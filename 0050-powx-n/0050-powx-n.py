class Solution:
    def myPow(self, x, n):

        def f(a,b):
            if(b==0):
                return 1
            if(b==1):
                return a
            if(b<0):
                b=abs(b)
                ans=f(a,b//2)
                if(b%2==0):
                    return(1/(ans*ans))
                else:
                    return(1/(a*ans*ans))
            ans=f(a,b//2)
            if(b%2==0):
                return(ans*ans)
            else:
                return(a*ans*ans)
        r=f(x,n)
        return(r)
        