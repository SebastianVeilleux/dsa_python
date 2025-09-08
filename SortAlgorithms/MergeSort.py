my_list = [9,6,7,5,4,3,2,0]

def merge_sort(numbers: list):
    
    #Base Case
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers)//2
    #Separation
    left = numbers[:mid]
    right = numbers[mid:]
    
    ordered_left = merge_sort(left)
    ordered_right = merge_sort(right)
    
    return merge(ordered_left, ordered_right)
    
    
def merge(left: list, right: list):
    merged_list = []
    
    i = j = 0
    
    while(i < len(left) and j < len(right)):
        if (left[i] < right[j]):
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
        
    if i==len(left):
        merged_list.extend(right[j:])
    else:
        merged_list.extend(left[i:])
        
    return merged_list


print(merge_sort([5,9,8,2,1,0,112,332]))