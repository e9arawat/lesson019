# Foundations of Python - Part 3

**1. Nest list comprehensions**

Write a function `nested_prime()` to generate a list of prime numbers upto $n$ using only a nested list comprehension

**2. Reverse a string**

Write a function `old_school_reverse()` that reverses a string or number without using `.reverse()` or `[::-1]` slicing and returns any other value passed to the function as is.

```python
def old_school_reverse(n):
    return n
```

**3. Dictionary Comprehension with Conditional Logic**

Write a function `dict_a_noodle()` that ingests a dictionary and returns a dictionary such that `key: value` becomes the `value: key` if the key is a string and is unchanged if the key is anything other than a string.

```python
def dict_a_noodle(a):
    return a
```

**4. Fibonacci Squares**

Write a function `fib_squares()` that returns a list of numbers where each element is the number if the number is not a fibonacci number and the square of the number if the number is a fibonacci number for a given range of numbers.

```python
def fib_squares(a, b):
    return list(range(a, b+1))
```

```python
>>> fib_squares(2, 5):
[4, 9, 4, 25]
```

**5. Cataloging a list of lists**

Write a function `dict_of_lists()` that...
1. takes a deeply nested list of lists and flattens it out,
2. ignores any dict elements, and
3. returns a dictionary where the key is value and the value is the count of each item in the flattened list.

Use recursion to flatten the list.

```python
def dict_of_lists(data):
    return data
```

```python
>>> data = [[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]
>>> list_of_lists(data)
{1: 3, 2: 2, 3: 1, 4: 1, 5: 2, 6: 2, 7: 1, 8: 3, 9: 2, "a": 1, "b": 1, "ab": 1}
```

**6. Flattening a list of lists**

Write a function `list_of_lists()` that
1. takes a deeply nested list of lists and flattens it out,
2. ignores any dict elements, and
3. returns a sorted list of unique values of the combined list. 

Use recursion to flatten the list.

```python
def list_of_lists(data):
    return data
```

```python
>>> data = [[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]
>>> list_of_lists(data)
[1, 2, 3, 4, 5, 6, "a", "ab", "ab"]
```

**7. Complement of sets**

```python
def set_complement(*args, verbose=False):
    """
    Return a set of the complement of all the lists provided in *args for every combination of lists

    Include the lists considered in each result when verbose=True
    """
```

```
>>> set_complement(list1, list2, list3)
[
    [2, 4],
    [2, 4],
    [4],
    [2],
    [1, 2, 3, 4],
    [1, 3]
    [1, 2, 3]
]
```

**8. Intersecting sets**

```python
def set_intersection(*args, verbose=False):
    """
    Return a list of lists of
    - the intersection of all sets
    - the intersection of every possible combination of sets from all sets provided

    Include the lists considered in each result when verbose=True
    """
```

**9. Compare dictionaries**

```python
def dict_compare(*args):
    """
    Using recursion, return a list of all combinations of dictionaries that
    are identical to each other for all combinations of dictionaries provided.

    Equivalence requires that all included lists are also identical in content
    but not in sortedness.

    Make no assumption about the order of keys or the depth of the data.

    Your compare function must use recursion.
    """  
```

**10. Create a dict from two given lists**

Write a function `dict_from_lists()` that
1. takes 2 lists
2. create a dict such that the keys are elements from the first list and the values are elements from the second list


```python
def dict_from_lists(list1, list2):
    return data
```

```python
>>> list1 = [1, 2, 3]
>>> list2 = ["a", "b", "c"]
>>> dict_from_lists(list1, list2)
{"1": "a", "2": "b", "3": "c"}
```

**11. Create your own secret message**

One classic method for composing secret messages is called a square code.  The spaces are removed from the english text and the characters are written into a square (or rectangle).  For example, the sentence "If man was meant to stay on the ground god would have given us roots" is 54 characters long, so it is written into a rectangle with 7 rows and 8 columns.  

    ifmanwas  
    meanttos        
    tayonthe  
    groundgo  
    dwouldha  
    vegivenu  
    sroots  

The coded message is obtained by reading down the columns going left to right.   For example, the message above is coded as:  
imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau

Write to function to take a message in plain english and return your secret message. Limit the length of the incoming message to 81 characters.

```python
def my_secret(message):
    return secret_message
```

**12. Create phone "words"**  

Each number on the telephone dial (except 0 and 1) corresponds to three alphabetic characters. Those correspondences are:  
 2 ABC  
 3 DEF  
 4 GHI  
 5 JKL  
 6 MNO  
 7 PRS  
 8 TUV  
 9 WXY  
Given a seven digit telephone number, print all 2187 possible "words" that number spells. The input will be one or more seven digit integers. The output should be a dict with the inputs as keys and a list of all possible words. Since the digits 0 and 1 have no alphabetic equivalent, an input number which contains those digits should be rejected with an empty list output.

```python
def phone_words(ph1, ph2):
    return 
```
```
>>> output = phone_words(1234567, 2345678)
>>> output: {"1234567": [], "2345678": ["ADGJMPT", ...]}
```