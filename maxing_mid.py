def mid_max(inter):
    array = [-1, inter, -1, -1, inter, inter, -1, -1, inter, -1, inter, inter, -1]
    curele = bestele = array[0]

    for y in array[1:]:
        if curele < 0:
            curele = y

        else:
            curele = curele + y

        if curele > bestele:
            bestele = curele

    return bestele

intern = int(input("Enter a number: "))
print(f" mid_max({intern}) = {mid_max(intern)}")