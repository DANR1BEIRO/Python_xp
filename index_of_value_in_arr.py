arr = [1, 2, 3, 4, 10, -70]

for i in range(len(arr)):
    if arr[i] == 10:
        print(i)
        
def findIndex(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

print(findIndex(arr, 10))

def find_index(arr, target):
    return arr.index(target) if target == 10 else -1

print(find_index(arr, 10))