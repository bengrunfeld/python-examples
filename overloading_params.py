#! /usr/bin/python

def pay_rent(balance, payment=5, message="Rent paid."):
    balance += payment
    print "Balance:", balance, "Payment:", payment, "Status:", message

pay_rent(1)
pay_rent(1, 50)
pay_rent(1, 500, "Ok, I'm broke now")
