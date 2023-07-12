# Name: Jim Telles
# OSU Email: tellesj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date: 7/11/23
# Description: Python review and introduction to following directions for this course.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr):
    """
    Function to return the minimum and maximum values from an array of any length.
    """
    max_num = arr[0]
    min_num = arr[0]
    num_of_elements = StaticArray.length(arr)
    for ind in range(num_of_elements):
        if num_of_elements == 1:
            max_num = (arr[ind])
            min_num = (arr[ind])
        # elif arr[ind] == arr[ind + 1]:
        #     max_num = (arr[ind])
        #     min_num = (arr[ind])
        elif arr[ind] > max_num:
            max_num = (arr[ind])
        elif arr[ind] < min_num:
            min_num = (arr[ind])
    return min_num, max_num


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr):
    """
    Function takes in a list of integers, determines if an integer is a multiple of 3, 5, or
    both, and assigns a string accordingly to that index position in a new list.
    """
    num_of_elements = StaticArray.length(arr)
    new_arr = StaticArray(num_of_elements)
    for ind in range(num_of_elements):
        if arr[ind] % 5 == 0 and arr[ind] % 3 == 0:
            new_arr.set(ind, "fizzbuzz")
        elif arr[ind] % 3 == 0:
            new_arr.set(ind, "fizz")
        elif arr[ind] % 5 == 0:
            new_arr.set(ind, "buzz")
        else:
            new_arr.set(ind, arr[ind])
    return new_arr




# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr):
    """
    Funciton takes in an array and reverses it, in place.
    """
    num_of_elements = arr.length()
    cnt = 0
    for r in range((num_of_elements) - 1, -1, -1):
        while cnt < num_of_elements / 2:
            arr[cnt], arr[r] = arr[r], arr[cnt]
            cnt = cnt + 1
            r = r - 1


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int):
    """
    Function takes in two integers and creates an array that goes from the start value to the
    end value.
    """
    if end == start:
        arr = StaticArray(1)
        arr[0] = start
    elif start == 0:
        size = abs(end) + 1
        arr = StaticArray(size)
        if end < 0:
            for index in range(size):
                arr[index] = start
                start = start - 1
        else:
            arr = StaticArray(size)
            for index in range(size):
                arr[index] = start
                start = start + 1
    else:
        size = abs(end - start) + 1
        arr = StaticArray(size)
        if end < start:
            for index in range(size):
                arr[index] = start
                start = start - 1
        else:
            arr = StaticArray(size)
            for index in range(size):
                arr[index] = start
                start = start + 1
    return arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    Function checks an array to see if it's sorted, and returns a value of 1 if the list is
    sorted in an ascending order, -1 if the list is sorted in a descending order, and 0 if the
    list is not sorted. A list with a single element is assigned a value of 1.
    """
    num_of_elements = arr.length()
    # comparison = StaticArray()
    # comparsion = arr
    if (num_of_elements) == 1:
        return 1
    elif arr[0] > arr[1]:
        for i in range(num_of_elements):
            x = 1
            while arr[i] > arr[x] and x < num_of_elements - 1:
                x = x + 1
                i = i + 1
            if x == num_of_elements - 1 and arr[i] > arr[x]:
                return -1
            else:
                return 0
    elif arr[0] < arr[1]:

        for i in range(num_of_elements):
            x = 1
            while arr[i] < arr[x] and x < num_of_elements - 1:
                x = x + 1
                i = i + 1
            if x == num_of_elements - 1 and arr[i] < arr[x]:
                return 1
            else:
                return 0
    elif arr[0] == arr[1]:
        for i in range(num_of_elements):

            x = 1
            while arr[x] == arr[i] and x < num_of_elements - 1:
                x = x + 1
                i = i + 1
                if arr[x] > arr[i]:
                    print(x)
                    for i in range(num_of_elements - i):
                        x = x
                        i = i
                        while arr[i] > arr[x] and x < num_of_elements - 1:
                            x = x + 1
                            i = i + 1
                        if x == num_of_elements - 1 and arr[i] > arr[x]:
                            return 1
                        else:
                            return 0
                elif arr[x] < arr[i]:
                    for i in range(num_of_elements):
                        x = x
                        i = i
                        while arr[i] < arr[x] and x < num_of_elements - 1:
                            x = x + 1
                            i = i + 1
                        if x == num_of_elements - 1 and arr[i] < arr[x]:
                            return -1
                        else:
                            return 0



# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple[object, int]:
    """
    Function takes an array and determines if there are elements repeated, if so, how many times, and which element
    was repeated the most.
    """
    final_mode = arr[0]
    final_freq = 1
    final_mode1 = 1
    final_freq1 = 1
    num_of_elements = arr.length()
    cnt = 0
    cntb = 1
    if num_of_elements == 1:
        return arr[0], 1
    else:
        for i in range(num_of_elements - 1):
            if arr[i] == arr[i + 1]:
                cnt = cnt + 1
                final_freq = cnt + 1
                final_mode = arr[i]
                # print(final_mode)
                # print(final_freq)
            else:
                if cntb <= cnt:
                    cntb = cnt
                    cnt = 0
                    final_freq1 = final_freq
                    final_mode1 = arr[i]
                else:
                    final_freq = 0

    if final_freq > final_freq1:
        return final_mode, final_freq
    elif final_freq == final_freq1:
        return final_mode1, final_freq
    elif final_freq < final_freq1:
        return arr[0], 1


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    Function takes in an ordered array, removes any duplicate elements, and returns a new array while keeping
    the orginal array intact.
    """
    num_of_elements = arr.length()
    new_arr = StaticArray(num_of_elements)
    counter = 0
    second_counter = 1
    if num_of_elements == 1:
        new_arr[0] = arr[0]
        return new_arr
    elif num_of_elements == 2:
        if arr[0] != arr[1]:
            new_arr = arr
            return new_arr
        else:
            transfer_arr = StaticArray(1)
            transfer_arr.set(0, arr[0])
        return transfer_arr
    else:
        for i in range(num_of_elements - 1):
            if arr[i] != arr[i + 1]:
                if counter + 2 == num_of_elements -1:
                    new_arr.set(1, arr[2])
                    second_counter = 2
                else:
                    new_arr[counter] = arr[i]
                    counter = counter + 1
            elif arr[i] == arr[i + 1] and counter + second_counter == num_of_elements:
                second_counter = counter + 1
                new_arr[counter + 1] = arr[i]
            elif arr[i] == arr[i + 1]:
                new_arr[counter] = arr[i]
                second_counter = counter + 1
        transfer_arr = StaticArray(second_counter)
        for j in range(second_counter):
            transfer_arr.set(j, new_arr[j])
        return transfer_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    num_of_elements = arr.length()
    new_arr = StaticArray(num_of_elements)
    for index in range(arr.length()):
        new_arr.set(index, (arr[index] * arr[index]))
    num_of_elements = arr.length()
    cnt = 0
    for r in range((num_of_elements) - 1, -1, -1):
        while cnt < num_of_elements / 2:
            new_arr[cnt], new_arr[r] = new_arr[r], new_arr[cnt]
            cnt = cnt + 1
            r = r - 1
    return new_arr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
