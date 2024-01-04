"""Foundations of Python - Part 3"""


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
    ans = [[x for x in args[i] if x not in args[j]] for i in range(size) for j in range(size) if [x for x in args[i] if x not in args[j]]]
    if verbose:
        ans += [args[i] for i in range(size)]
    return ans

def set_intersection(*args, verbose=False):
    """Intersecting sets"""
    size = len(args)
    list1 = args[0]
    list1 = [x for i in range(1,size) for x in set(list1) if x in set(args[i])]
    list1 = list(set(list1))
    ans= [[x for x in set(args[i]) if x in set(args[j])] for i in range(size-1) for j in range(i+1, size)]
    ans.append(list1)
    if verbose:
        ans += [args[i] for i in range(size)]
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
    print(set_complement([1,2,3,4],[1,3],[1,2,3]))
    print(set_intersection([1,1,5,4,2,3,4],[1,5,1,3],[1,5,2,3]))
