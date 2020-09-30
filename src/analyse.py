def chk(func,*args,**kwargs):
    return(questions[func](args))

def check_even(n):          #Checks if a number is even or not
    ls = []
    try:
        for i in (n[0]):
            ls.append(bool(not i%2))
        return(ls)
    except ValueError:
        print("Error")

def bubble_sort(ar):       #Bubbles sorts the array
    ls = []
    ar = ar[0]
    try:
        for arr in ar:
            for i in range(len(arr)):
                for k in range(len(arr)-i-1):
                    if arr[k] > arr[k+1]:
                       arr[k] ,arr[k+1] = arr[k+1] ,arr[k]
            ls.append(arr)
        return(ls)
    except ValueError:
        print("Error")


def fibonacci(inp):
    ls = []
    p = inp[0]
    try:
        for n in p:
            #n = int(n[0])
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
        return(ls)
    except ValueError:
        print("Error")

def palin(s):
    s = s[0]
    ls = []
    try:
        for i in s:
            ls.append(i==i[::-1])
        return(ls)

    except ValueError:
        print("Wrong Data Type")

questions = { 1 : check_even,
              2 : bubble_sort,
              3 : fibonacci,
              4 : palin
             }
testcases = {
              1 : [1,2,3,4,10,12,83,12],
              2 : [ [1,2,3,45,2,32,3] , [1,12,3,213,22,34,21,45,6,7,894,34,23,244,34,34,4343,4343] , [0,0,0,0,0,0,0,0,0] , [12,11,10,9,8,7,6,5,4,3,2,1,0] , [21312434,3453646,3453453,324534,25435345,45345345,543545,345345435,34534534,546865,6586856,8657567,765756,4645645,4564654,56656] ],
              3 : [10 , 32, 21, 12 , 55],
              4 : [ 'pop' , 'malayalam' , 'qwerty' , 'popopopop','ewruiu','miami' ]

            }
