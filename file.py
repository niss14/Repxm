class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        outlist = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if (nums[i]+nums[j]==target and i != j):
                    outlist = [i, j]
                    return outlist