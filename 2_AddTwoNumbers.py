def addTwoNumbers(l1, l2):
    if l1 == []:
        l1 = [0]
    l3 = []
    l4 = []
    output = []
    for i in range(len(l1)):
        l3.append(str(l1[-1 - i]))
    for i in range(len(l2)):
        l4.append(str(l2[-1 - i]))
    l3 = "".join(l3)
    l4 = "".join(l4)
    sumString = [*str(int(l3) + int(l4))]
    for i in range(len([*str(int(l3) + int(l4))])):
        output.append(int(sumString[-1 - i]))
    return output


print(addTwoNumbers([905], [1032]))
