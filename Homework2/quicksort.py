import time

def get_pivot(array, method):
    if method == 1:
        pivot = array.pop(0)
    if method == 2:
        pivot = array.pop()
        switch = array.pop(0)
        array.append(switch)
    if method == 3:
        first = array[0]
        last = array[len(array) -1]
        mid_i = int(len(array)/2) + 1 if len(array) % 2 != 0 else len(array)/2
        middle = array[mid_i]
        if first < middle and first > last:
            pivot = array.pop(0)
        elif middle > first and middle < last:
            pivot = array.pop(mid_i)
            switch = array.pop(0)
            array.insert(switch, mid_i - 1)
        else:
            pivot = array.pop()
            switch = array.pop(0)
            array.append(switch)

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
            if len(larger_array) > 1:
                larger_array.append(larger_array.pop(0))
    if len(smaller_array) > 1:
        smaller_array.insert(0, smaller_array.pop())
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
    # sorted_array, comparisons1 = quick_sort(large_array, 1)
    sorted_array, comparisons = quick_sort(large_array, 2)
    # sorted_array, comparisons = quick_sort(large_array, 3)
    print comparisons
