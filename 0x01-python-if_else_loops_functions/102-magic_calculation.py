#!/usr/bin/python3
# Author - Bamidele Adefolaju

def magic_calculation(a, b, c):
    """Match bytecode provided by Holberton School."""
    if a < b:
        return (c)
    return (a + b) if c > b else (a*b - c)
