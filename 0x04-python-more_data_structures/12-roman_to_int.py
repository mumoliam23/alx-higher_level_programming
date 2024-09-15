#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_number = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
    equivalent_int = 0
    prev_int_value = 0
    for roman_numeral in reversed(roman_string):
        int_value = roman_number.get(roman_numeral, 0)
        if int_value >= prev_int_value:
            equivalent_int += int_value
        else:
            equivalent_int -= int_value
        prev_int_value = equivalent_int
    return equivalent_int
