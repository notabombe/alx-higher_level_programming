#!/usr/bin/python3
# Author - Tolulope Fakunle
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print(f"{chr(letter)}", end="")
