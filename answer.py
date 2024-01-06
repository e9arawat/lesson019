"""Foundations of Python - Part 3"""

import math


def nested_prime(n):
    """list comprehension to find all prime numbers upto n"""
    return [
        i
        for i in range(2, n + 1)
        if all((i % j != 0) for j in range(2, int(i**0.5) + 1))
    ]


def old_school_reverse(n):
    """function to reverses a string or number"""
    num = str(n)
    num_list = [num[i] for i in reversed(range(0, len(num)))]
    num = "".join(num_list)
    return num


def dict_a_noodle(a):
    """function that ingests a dictionary and returns a dictionary such that
    key: value becomes the value: key if the key is a string and is unchanged
    if the key is anything other than a string."""

    return {
        value if key == str(key) else key: key if key == str(key) else value
        for key, value in a.items()
    }


def fib_squares(a, b):
    """that returns a list of numbers where each element is the number if the number
    is not a fibonacci number and the square of the number if the number is a fibonacci
    number for a given range of numbers."""
    start, end = 1, a
    if b:
        start, end = a, b

    x, y = 0, 1
    fibonacii_list = [0, 1]
    while y <= end:
        fibonacii_list.append(x + y)
        x, y = y, fibonacii_list[-1]

    fib_squares_list = [
        i**2 if i in fibonacii_list else i for i in range(start, end + 1)
    ]

    return fib_squares_list


def flatten(input_list):
    """function to flatten a nested list"""
    ans = []
    for i in input_list:
        if isinstance(i, dict):
            continue
        if isinstance(i, list):
            ans += flatten(i)
        else:
            ans.append(i)
    return ans


def dict_of_lists(input_list):
    """Cataloging a list of lists"""
    flatten_list = flatten(input_list)
    ans = {}
    for i in flatten_list:
        if i not in ans:
            ans[i] = flatten_list.count(i)
    return ans


def unique_flatten(ans, input_list):
    """function to find uniques elements in a nested elements"""
    for i in input_list:
        if str(type(i)) == "<class 'dict'>":
            continue
        if str(type(i)) == "<class 'list'>":
            unique_flatten(ans, i)
        elif i not in ans:
            ans.append(i)


def list_of_lists(input_list):
    """Flattening a list of lists"""
    ans = []
    unique_flatten(ans, input_list)
    return ans


def set_complement(*args, verbose=False):
    """Complement of sets"""
    size = len(args)
    ans = [
        [x for x in args[i] if x not in args[j]]
        for i in range(size)
        for j in range(size)
        if [x for x in args[i] if x not in args[j]]
    ]
    if verbose:
        ans += [args[i] for i in range(size)]
    return ans


def set_intersection(*args, verbose=False):
    """Intersecting sets"""
    list1 = args[0]
    list1 = [x for i in range(1, len(args)) for x in set(list1) if x in set(args[i])]
    list1 = list(set(list1))
    ans = [
        [x for x in set(args[i]) if x in set(args[j])]
        for i in range(len(args) - 1)
        for j in range(i + 1, len(args))
    ]
    ans.append(list1)
    if verbose:
        ans += [args[i] for i in range(len(args))]
    return ans

def dict_compare(*args):
    def compare_dicts(dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            for x in dict1:
                if x in dict2:
                    if not compare_dicts(dict1[x], dict2[x]):
                        return False
                else:
                    return False
            return True
        elif isinstance(dict1, list) and isinstance(dict2, list):
            return sorted(dict1) == sorted(dict2)
        else:
            return dict1 == dict2
    
    def find_identical_combinations(args_list, current_combination):
        if len(args_list) == 0:
            identical_combinations.append(current_combination.copy())
            return
        
        current_dict, rest_of_dicts = args_list[0], args_list[1:]
        
        for i, dict in enumerate(rest_of_dicts):
            if compare_dicts(current_dict, dict):
                find_identical_combinations([current_dict] + rest_of_dicts[:i] + rest_of_dicts[i+1:], current_combination + [dict])
        
        find_identical_combinations(rest_of_dicts, current_combination + [current_dict])
    args_list = list(args)
    identical_combinations = []
    find_identical_combinations(args_list, [])
    return identical_combinations
        

def dict_from_lists(list1, list2):
    """function to return dictionary from two lists"""
    if len(list1) != len(list2):
        return {}
    ans = {list1[i]: list2[i] for i in range(len(list1))}
    return ans


def my_secret(input_message):
    """function to return secret message"""
    message = input_message.replace(" ", "").lower()
    columns = math.ceil(len(message) ** 0.5)
    grid = []
    i = 0
    for _ in range(columns - 1):
        grid.append(message[i : i + columns])
        i += columns

    secret_message = ""
    for i in range(columns + 1):
        for j in grid:
            if i < len(j):
                secret_message += j[i]
        secret_message += " "
    return secret_message


def all_combinations(alphabetic, num, combinations_list, current_str):
    """function to find all the combination on a number"""
    if not num:
        combinations_list.append(current_str)
        return []
    all_combinations(
        alphabetic, num[1:], combinations_list, current_str + alphabetic[int(num[0])][0]
    )
    all_combinations(
        alphabetic, num[1:], combinations_list, current_str + alphabetic[int(num[0])][1]
    )
    all_combinations(
        alphabetic, num[1:], combinations_list, current_str + alphabetic[int(num[0])][2]
    )
    return combinations_list


def phone_words(*args):
    """Create phone words"""
    alphabetic = {
        2: "ABC",
        3: "DEF",
        4: "GHI",
        5: "JKL",
        6: "MNO",
        7: "PRS",
        8: "TUV",
        9: "WXY",
    }
    ans = {}
    for i in args:
        if "0" in str(i) or "1" in str(i):
            ans[i] = []
            continue
        combinations = all_combinations(alphabetic, str(i), [], "")
        ans[i] = combinations
    return ans


if __name__ == "__main__":
    print(nested_prime(23))
    print(old_school_reverse("123456"))
    print(dict_a_noodle({10: {1: "akash"}, 2: "rawat", 3: 3, "kirti": 1}))
    print(fib_squares(2, 5))
    data = [
        [[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]],
        [5, 2, 1],
        1,
    ]
    print(dict_of_lists(data))
    print(list_of_lists(data))
    print(set_complement([1, 2, 3, 4], [1, 3], [1, 2, 3]))
    print(set_intersection([1, 1, 5, 4, 2, 3, 4], [1, 5, 1, 3], [1, 5, 2, 3]))
    print(dict_compare({'a': 1, 'b': [2, 3]},{'b': [3, 2], 'a': 1},{'c': 4, 'd': {'e': 5}}))
    print(dict_from_lists([1, 2, 3], ["a", "b", "c"]))
    print(my_secret("If man was meant to stay on the ground god would have given us roots"))
    print(phone_words(1234567, 2345678))
