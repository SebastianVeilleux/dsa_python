def binary_search(values: list, target: int) -> int:
    left = 0
    right = len(values) - 1
    mid = (left+right) // 2
    
    while(left <= right):
        mid = (left+right) // 2
         
        if(values[mid] == target):
            return mid
        
        if(values[mid] > target):
            right = mid - 1
        elif(values[mid] < target):
            left = mid + 1
            
    return -1

values = [1,2,3,4,5,6,7]
print(binary_search(values, 2))