#! /usr/bin/python

def add_input(tweet, record=None):
    if record is None:
        record = []
    record.append(tweet)
    return record

print add_input("I'm so happy")
print add_input("Are you happy?")
print add_input("Goodbye")
