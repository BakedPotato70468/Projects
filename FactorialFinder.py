import random
number = 10
result = 0
ans = 0
def factorial(number):
    global result , ans
    lower = number-1
    result = number * lower
    i = number
    while i > 0:
        lower -= 1
        if lower == 0:
            break
        else:
            ans = result*lower
            result = ans
            i-=1
    print(ans)


factorial(number)



