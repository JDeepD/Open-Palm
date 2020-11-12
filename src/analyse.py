"""This module will be used for running and analysing test cases on
the scripts given by the user."""


def chk(func, *args):
    return questions[func](args)


def check_even(n):   # Checks if a number is even or not
    """This is `Open-Palm's` function that checks if a
    number is even or odd.
    The input `n` is a tuple of single argument. Therefore only the
    first (0 th argument) is accessed.
    The first argument of the tuple i.e `n[0]`
    is a list that contains testcases.
    This function iterates through that list
    and checks individually if each element is odd or even.
    It returns a new list `ls` with corresponding results of
    the input.
    For example :
    If n = ([1,2,4,5],)
    then n[0] = [1,2,4,5]
    Iterating though each element of n[0] and checking if
    its even or not, we get that

    1 -> odd
    2 -> even
    4 -> even
    5 -> odd

    Therefore it returns the list : [False,True,True,False]
    (Returns True if even, else False)
    """
    ls = []
    try:
        for i in (n[0]):
            ls.append(bool(not i % 2))
        return ls
    except ValueError:
        print("Error")


def bubble_sort(ar):     # Bubbles sorts the array
    """This is `Open-Palm's` function that sorts an array
    The input `ar` is a tuple of single argument. Therefore only the
    first (0 th argument) is accessed.
    The first argument of the tuple i.e `ar[0]`
    is a list that contains testcases.
    Here the first argument is a list of multiple list
    For example:
    ar = (
          [
            [14,3,5,2],
            [1,5,2],
            [2,23,2]
          ]
         )

    Therefore, ar[0] = [
                        [14,3,5,2],
                        [1,5,2],
                        [2,23,2]
                       ]

    Iterating through ar[0], we sort the individual arrays
    and store them in a new array called ls in the same order
    as input.
    In the end, we return our new array `ls`.
    """


    ls = []
    ar = ar[0]
    try:
        for arr in ar:
            for i in range(len(arr)):
                for k in range(len(arr)-i-1):
                    if arr[k] > arr[k+1]:
                        arr[k], arr[k+1] = arr[k+1], arr[k]
            ls.append(arr)
        return ls
    except ValueError:
        print("Error")


def fibonacci(inp):
    """
    This is `Open-Palm's` function that generates
    a fibonacci series upto `inp` th digit.The input `inp` is
    a tuple containing a single element.Therefore only the
    first (0 th argument) is accessed.
    The first argument of the tuple i.e `inp[0]`.
    inp[0] is a list.
    Then, `inp[0]` is traversed and then
    for each item, the fibonacci series is generated and the
    result is stored in a list `ls`.After completion, the list
    `ls` is returned.
    For example:
    inp = (
            [3, 9, 44, 5]
          )
    inp[0] = [3, 9, 44, 5]
    """

    ls = []
    p = inp[0]
    try:
        for n in p:
            # n = int(n[0])
            a = 0
            b = 1
            if n < 0:
                print("Incorrect input")
            elif n == 0:
                return a
            elif n == 1:
                return b
            else:
                for i in range(2,n+1):
                    c = a + b
                    a = b
                    b = c
                ls.append(b)
        return ls
    except ValueError:
        print("Error")


def check_palin(s):
    """
    This is `Open-Palm's` function that checks if elements of
    a given list of strings `s` is a palindrome or not.
    The input `inp` is a tuple containing a single
    element.Therefore only the
    first (0 th argument) is accessed.
    The first argument of the tuple i.e `s[0]`.
    s[0] is a list of strings.
    Then, elements of `s[0]` is traversed and checked
    if the element is a palindrome or not.
    The result is stored in a new list `ls`.
    This new list is returned in the end.
    For example:
    s = (
           ['malayalam', 'pop', 'linux']
        )
    s[0] =  ['malayalam', 'pop', 'linux']
    """
    s = s[0]
    ls = []
    try:
        for i in s:
            ls.append(i == i[::-1])
        return(ls)

    except ValueError:
        print("Wrong Data Type")



"""This dictionary stores the `question code` as key
and the function instance (Open-Palm's function) as its value
This means that accessing one value of the `questions` dictionary
will give the instance of the function.
For example:

~ question[1] is equivalent to `check_even`

To call the function `check_even` with some parameters, we call
it in this waya (args is the parameters given to `check_even` func):

~ questions[1](args)  is equivalent to `check_even(args)`
"""
questions = {
             1: check_even,
             2: bubble_sort,
             3: fibonacci,
             4: check_palin
            }

"""
These are the test cases on which `Open-Palm's` program and student's
program will be tested on.Provided, Open-Palm's program will always be
the correct output, therefore our `expected result` will be the ones
that are given by the *above functions*(Open-Palm's function)
The testcases have been stored in the form of a dictionary for easy
access the above functions
"""
testcases = {
              1: [1, 2, 3, 4, 10, 12, 83, 12],
              2: [
                  [1, 2, 3, 45, 2, 32, 3],
                  [1, 12, 3, 213, 22, 34, 21, 45, 6, 7, 894, 34, 23, 244, 34, 34, 4343, 4343],
                  [123, 123241324, 123, 4234, 12, 3, 4345, 12342, 433242, 234],
                  [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
                  [21312434, 3453646, 3453453, 324534, 25435345, 45345345, 543545, 345345435, 34534534, 546865, 6586856, 8657567, 765756, 4645645, 4564654, 56656]
                 ],
              3: [10, 32, 21, 12, 55],
              4: ['pop', 'malayalam', 'qwerty', 'popopopop', 'ewruiu', 'miami']
            }
