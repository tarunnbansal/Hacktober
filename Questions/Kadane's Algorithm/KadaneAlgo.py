import math

def largestContinuosSum(arr):
    cur_max=-math.inf
    new_max=0
    
    for i in arr:
        new_max=new_max+i
        cur_max=max(cur_max,new_max)
        
        if new_max<0:
            new_max=0
    return cur_max

array=[int(x) for x in input("Enter the array to find its max contiguous sum : ").split()]
print(largestContinuosSum(array))
