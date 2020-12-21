#!/usr/bin/env python3

from random import randint
from sys import argv
from re import match
from sys import exit

if len(argv) != 1:
    password_length = argv[1]
    if not match("^([1-9]|[1-9][0-9])$", password_length):
        print("Password length is invalid!")
        exit()
else:
    # Default Password Length
    password_length = 16

alphanumeric = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"

alphanumeric = alphanumeric.split(" ")

def get_random_char():
    return alphanumeric[randint(0, len(alphanumeric) - 1)]

random_chars = []

password_length = int(password_length)
for i in range(password_length):
    random_chars.append(get_random_char())

insecure_password = "".join(random_chars)

print(insecure_password)
if password_length < 16:
    print("Your password is dangerously short.")
