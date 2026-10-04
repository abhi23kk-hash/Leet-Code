class Solution(object):
    def sortedSquares(self, nums):
        l=0
       
        result=[0]*len(nums)
        # result=[]
        r=len(nums)-1
        pos=r
        while(l<=r):
            l_s=nums[l]**2
            r_s=nums[r]**2
            if l_s<r_s:
                result[pos]=r_s
                pos-=1
                r-=1
            else:
                result[pos]=l_s
                pos-=1
                l+=1
        return result
        



        