def lengthOfLongestSubstring(s):
    sequence = [*s]
    answer = []
    length = []
    if len(sequence) == 1:
        return 1
    if len(sequence) > 1:
        answer.append(sequence[0])
        sequence = sequence[1:]
        for i in range(len(sequence)):
            if sequence[i] not in answer:
                answer.append(sequence[i])
            else:
                for j in range(len(answer)):
                    j = answer.index(sequence[i])
                del answer[: j + 1]
                answer.append(sequence[i])
            length.append(len(answer))
            print(answer)
        length.sort()
        if len(length) != 1:
            return length[-1]
        else:
            return length[0]
    else:
        return 0


print(lengthOfLongestSubstring("ckilbkd"))
