class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index = {}

        for i in range(len(nums)):
            if nums[i] in index and i - index[nums[i]] <= k:
                return True

            index[nums[i]] = i

        return False