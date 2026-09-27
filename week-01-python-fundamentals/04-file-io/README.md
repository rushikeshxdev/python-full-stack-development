# Task 4 — File I/O

## What is File I/O?

File I/O means File Input/Output.

It allows a Python program to:
- Create files
- Read data from files
- Write data to files
- Append new data
- Modify stored data

## Common File Modes

- `r` → Read
- `w` → Write / overwrite
- `a` → Append
- `x` → Create a new file

## Recommended Pattern

```python
with open("file.txt", "r") as file:
    data = file.read()