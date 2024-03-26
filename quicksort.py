def quicksort_Toni(array):
    if len(array) < 2:
        return array
    barrier_element = array[0]
    less = [i for i in array[1:] if i < barrier_element]
    equals = [barrier_element] * array.count(barrier_element)
    more = [i for i in array[1:] if i > barrier_element]
    return quicksort_Toni(less) + equals + quicksort_Toni(more)


print(quicksort_Toni([1, 4, 5, 2, 3, 6, 7, 8, 53, 2]))
