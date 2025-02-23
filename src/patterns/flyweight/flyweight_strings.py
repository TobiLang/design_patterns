"""Flyweight module."""

# Python uses Flyweight for strings (string interning)
STRING_ONE = "hello"
STRING_TWO = "hello"
# True, because `str1` and `str2` point to the same string object
print(STRING_ONE is STRING_TWO)

# Flyweight only works with immutable objects
STRING_TWO = "new hello"
# False, because `str1` and `str2` no longer point to the same object
print(STRING_ONE is STRING_TWO)

# Reassigning to the same string value
STRING_TWO = "hello"
# True, because `str1` and `str2` now point to the same object again
print(STRING_ONE is STRING_TWO)
