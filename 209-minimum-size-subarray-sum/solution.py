class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        s=0
        minlen=len(nums)+1
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                minlen=min(minlen,r-l+1)
                s-=nums[l]
                l+=1
        if minlen==len(nums)+1:
            return 0
        else:
            return minlen
        
        