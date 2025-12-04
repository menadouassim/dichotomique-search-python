def dechatomique_search(list, target):
    not_found=True
    start=0
    end=len(list)-1
    mid=(start+end)//2
    while start<=end and not_found:
        if list[mid]==target:
            not_found=False
            return mid
        elif list[mid]<target:
            start=mid+1
            mid=(start+end)//2
        else:
            end=mid-1
            mid=(start+end)//2  
    return "target not found"
def linear_search(list, target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return "target not found"

# Example usage:
my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_value = 6
dechatomique_search_result = dechatomique_search(list=my_list, target=target_value)
linear_search_result = linear_search(list=my_list, target=target_value)
print(f"the deachatomic search result is {dechatomique_search_result}")          
print(f"the linear search result is {linear_search_result}")

