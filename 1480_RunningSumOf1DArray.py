class Solution:
    def runningSum(nums: list[int]) -> list[int]:
        for i in range(0, len(nums) - 1):
            nums[i + 1] = nums[i] + nums[i + 1]
        return nums

    print(runningSum([1, 2, 3, 4]))
