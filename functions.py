#! /usr/bin/python

def example_func(i):
    """This program illustrates the use of functions"""
    print i

talk = example_func
talk('hello')
print talk('hi')
