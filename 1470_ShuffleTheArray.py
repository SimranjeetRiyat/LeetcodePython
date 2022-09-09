class Solution:
    def shuffle(nums: list[int], n: int) -> list[int]:
        first_list = nums[:n]
        second_list = nums[n:]
        result = []
        for i in range(len(first_list)):
            result.append(first_list[i])
            result.append(second_list[i])
        return result

    print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
