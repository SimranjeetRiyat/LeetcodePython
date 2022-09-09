class Solution:
    def maximumWealth(accounts: list[list[int]]) -> int:
        values = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum = sum + accounts[i][j]
                if j == len(accounts[i]) - 1:
                    values.append(sum)
        values.sort()
        return values[-1]
