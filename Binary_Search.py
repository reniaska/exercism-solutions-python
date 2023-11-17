# https://exercism.org/tracks/python/exercises/binary-search

def find(search_list, value):
    highest = len(search_list) - 1
    lowest = 0
    while highest >= lowest:
        mid = (highest + lowest) // 2
        if search_list[mid] > value:
            highest = mid - 1
        elif search_list[mid] < value:
            lowest = mid + 1
        else:
            return mid
    raise ValueError("value not in array")
