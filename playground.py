arr1 = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,3]
arr3= [2,3,4,5]

def first_recurring_character(arr):
    register = {}
    for ele in arr:
        if ele not in register:
            register[ele] = ele
        else:
            return register[ele]


frc = first_recurring_character(arr3)
print(frc)
