# 1 version O(n^2)

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sort_selection(arr):
    newArr = []
    for k in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


a = [5, 2, 6, 8, 10]
print(sort_selection(a))

# 2 version
def sort_selection2(arr):
    N = len(arr)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if arr[k] < arr[pos]:
                arr[k], arr[pos] = arr[pos], arr[k]
    return arr

b = [4,5,2,7,8]
print(sort_selection2(b))





