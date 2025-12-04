import random
import time
def dechatomique_search(list, target):
    
    start=0
    end=len(list)-1
    
    while start<=end :
        mid=(start+end)//2
        if list[mid]==target:
            
            return mid
        elif list[mid]<target:
            start=mid+1
            
        else:
            end=mid-1
            
    return "target not found"
def linear_search(list, target):
    for i in range(len(list)):
        if list[i]==target:
            return i
    return "target not found"
def generate_sorted_list(size):
    return sorted(random.sample(range(1, size + 1), size))
# Example usage:
my_list = generate_sorted_list(1_000_000)
target_value = random.randint(1, 1_000_000)
time_start = time.time()
dechatomique_search_result = dechatomique_search(list=my_list, target=target_value)
time_end = time.time()
print(f"the deachatomic search result is {dechatomique_search_result} and it took {time_end - time_start} seconds")          
time_start = time.time()
linear_search_result = linear_search(list=my_list, target=target_value)
time_end = time.time()
print(f"the linear search result is {linear_search_result} and it took {time_end - time_start} seconds")

