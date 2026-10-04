class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x - diff in bobSet:
                return [x, x - diff]