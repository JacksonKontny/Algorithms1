import time

def get_pivot(array, method):
    if method == 1:
        pop_index = 0
    if method == 2:
        pop_index = len(array) - 1
    if method == 3:
        first = array[0]
        last = array[len(array) -1]
        mid_i = int(len(array)/2) + 1 if len(array) % 2 != 0 else len(array)/2
        middle = array[mid_i]
        if first < middle and first > last:
            pop_index = 0
        elif middle > first and middle < last:
            pop_index = mid_i
        else:
            pop_index = len(array) - 1
    print array
    pivot = int(array.pop(pop_index))
    first_element = array.pop(0)
    array.insert(pop_index, first_element)
    print array
    time.sleep(1)
    return pivot, array
            
def quick_sort(unsorted_array, method = 1):
    sorted_array = []
    if len(unsorted_array) <= 1:
        return unsorted_array, 0
    smaller_array = []
    larger_array = []
    comparisons = len(unsorted_array) - 1
    pivot_element, unsorted_array = get_pivot(unsorted_array, method) 
    for element in unsorted_array:
        if(int(element) > pivot_element):
            larger_array.append(element)
        else:
            smaller_array.append(element)
    a = len(smaller_array)
    b = len(larger_array)
    c = len(unsorted_array)
    sorted_smaller_array, comp_1 = quick_sort(smaller_array)
    sorted_larger_array, comp_2 = quick_sort(larger_array)
    for element in sorted_smaller_array:
        sorted_array.append(element)
    sorted_array.append(pivot_element)
    for element in sorted_larger_array:
        sorted_array.append(element)
    return sorted_array, comparisons + comp_1 + comp_2

with open('IntegerList.txt') as f:
    large_array = []
    for number in f.readlines():
        large_array.append(int(number))
    sorted_array, comparisons1 = quick_sort(large_array, 1)
    sorted_array, comparisons2 = quick_sort(large_array, 2)
    sorted_array, comparisons3 = quick_sort(large_array, 3)
    print 'first method: ', comparisons1
    print 'second method: ', comparisons2
    print 'third method: ', comparisons3


