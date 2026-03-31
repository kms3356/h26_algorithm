def getIndex(num_list, target):
    for i in range(len(num_list)):
        if num_list[i] == target:
            return i
    return "없음"

def getMax(num_list):
    max = num_list[0]
    for i in range(1,len(num_list)):
        if max < num_list[i]:
            max = num_list[i]
    return max        

def getMin(num_list):
    min = num_list[0]
    for i in range(1,len(num_list)):
        if min > num_list[i]:
            min = num_list[i]
    return min        

def countGT(num_list, target):
    count = 0
    for cur in num_list:
        if cur > target:
            count+=1
    return count        

def sumList(num_list):
    sum = 0
    for cur in num_list:
        sum += cur
    return sum    

def swapList(num_list):
    mid = (len(num_list)//2)
    for i in range(mid):
        num_list[i], num_list[-1-i] = num_list[-1-i], num_list[i]    

nums = [23,45,27,11,25,65,78]
print(getIndex(nums,11))
print(getMax(nums))
print(getMin(nums))
print(countGT(nums,42))
print(sumList(nums))
swapList(nums)
print(nums)