class Solution(object):
    def isPalindrome(self, s):
        s.replace(" ","")
        a=""
        flag=0
        for i in s:
            if i.isalnum():
                a+=i
        b=a.lower()
        l=0
        r=len(b)-1
        while(l<=r):
            if b[l]!=b[r]:
                flag=1
                return False
            else:
                l+=1
                r-=1
        if flag==0:
            return True
           

        
        