def twoSum(nums, target):
    for i in range(len(nums)):
        j = target - nums[i]
        if j in nums and nums.index(j) != i:
            ans = [i, nums.index(j)]
            ans.sort()
            return ans


print(twoSum([3, 3], 6))
