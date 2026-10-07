def after_max(inter):
    array = [-inter] + [1]*inter
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
print(f" mid_max({intern}) = {after_max(intern)}")