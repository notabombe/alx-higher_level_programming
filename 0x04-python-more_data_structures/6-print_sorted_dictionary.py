#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_ord = sorted(a_dictionary.keys())
    for i in list_ord:
        print(f"{i}: {a_dictionary.get(i)}")
