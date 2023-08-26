#!/usr/bin/python3
# Author - bamidele Adefolaju

def remove_char_at(str, n):
    return str if n < 0 else (str[:n] + str[n+1:])
