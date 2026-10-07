import random as r
def max_all(array):
    curele = bestele = array[0]

    for y in array[1:]:
        if curele < 0:
            curele = y

        else:
            curele = curele + y

        if curele > bestele:
            bestele = curele

    return bestele

while True:
    print("\n1. Max_all \n2. Max_after")
    choose = int(input("\nEnter a option:"))
    
    if choose == 1:
        size_of_list = int(input("\nHow many numbers should be in the list? "))
        end_value = int(input("\nEnter end value: "))
    
    
        array = []
    
        for i in range(size_of_list - 1):
            array.append(r.randint(-end_value, end_value))
        
        print(f" max_all({array}) = {max_all(array)}")

    if choose == 2:
        intern = int(input("\nEnter a number: "))
        
        array = [-intern] + [1]*intern
       
        print(f"\n max_after({array}) = {max_all(array)}")

    else:
        print("Dude")