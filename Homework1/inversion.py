def splitter(number_array):
    array_length = len(number_array)
    first_half = number_array[0:array_length/2]
    second_half = number_array[array_length/2::]
    if array_length <= 20:
        return first_half, second_half
    else:
        return splitter(first_half), splitter(second_half)

def sorter(number_array):
    ...

with open('IntegerList.txt') as f:
    content = f.readlines()
    print splitter(content)

