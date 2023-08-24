#!/usr/bin/env python3

class MyString:
    def __init__(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueErrror("Value must be a string")
  
