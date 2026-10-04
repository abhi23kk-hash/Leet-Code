class Solution(object):
    def removeDuplicates(self, nums):
        l=0
        c=1
        for r in range(l+1,len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                nums[l]=nums[r]
        return l+1
