#https://exercism.org/tracks/python/exercises/list-ops

def append(list1, list2):
    return list1 + list2


def concat(lists):
    concatenated = []
    for list in lists:
        concatenated += list
    return concatenated


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    item_len = 0
    for item in list:
        item_len += 1
    return item_len


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial


def reverse(list):
    return [list[-i] for i in range(1, len(list) + 1)]