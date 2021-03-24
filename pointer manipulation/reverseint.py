class Solution:
    def reverse(self, x):
        ans=0
        if x > 0:
            ans=int(str(x)[::-1])
        elif x < 0:
            ans =-1* int(str(-1*x)[::-1])
        
        if (ans < -2**31) or (ans > (2**31-1)) or x==0:
            return 0
        else:
            return ans