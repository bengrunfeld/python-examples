#! /usr/bin/python
result = 0
my_list = [result, 100]

def my_math(a, b, c):
    """This function illustrates the use of return"""
    result = a + b + c
    my_list.append(result)
    return result

print my_math(5, 10, 15)
print my_list


