# Task 6 — Exception Handling

## What is Exception Handling?

Exception handling is a mechanism used to handle errors that occur while
a Python program is running, so that the program can respond gracefully
instead of terminating unexpectedly.

## Common Keywords

- `try` → code that may cause an exception
- `except` → handles the exception
- `else` → runs when no exception occurs
- `finally` → runs whether an exception occurs or not
- `raise` → manually raise an exception

## Common Exceptions

- `ValueError`
- `TypeError`
- `ZeroDivisionError`
- `FileNotFoundError`
- `KeyError`
- `IndexError`

## Basic Structure

```python
try:
    # risky code
except SomeException:
    # handle error