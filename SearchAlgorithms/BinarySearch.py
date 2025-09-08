my_list = [5,3,9,2,8,0,4]

def binary_search(nums: list, x):
    left = 0
    right = len(nums)-1
    
    while (left <= right):
        mid = (left + right ) // 2
        
        if nums[mid] == x:
            return mid
        
        if nums[mid] > x:
            left = mid + 1
        else:
            right = mid - 1 
       
    return -1

print(binary_search(my_list, 0))