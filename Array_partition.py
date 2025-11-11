class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            max_sum = min(nums(len(nums)-1)) + min(nums(len(nums)-(1-2*i)))
        return max_sum  