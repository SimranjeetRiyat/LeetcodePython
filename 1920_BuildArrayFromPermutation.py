class Solution:
    def buildArray(nums: list[int]) -> list[int]:
        solution = []
        for i in nums:
            solution.append(nums[nums[i]])
        return solution

    print(buildArray([5, 0, 1, 2, 3, 4]))
