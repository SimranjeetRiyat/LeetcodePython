class Solution:
    def finalValueAfterOperations(operations: list[str]) -> int:

        x = 0
        for i in range(len(operations)):
            if operations[i] == "--X":
                x = x - 1
            elif operations[i] == "X--":
                x = x - 1
            elif operations[i] == "++X":
                x = x + 1
            elif operations[i] == "X++":
                x = x + 1
        return x

    print(finalValueAfterOperations(["--X", "X++", "X++"]))
