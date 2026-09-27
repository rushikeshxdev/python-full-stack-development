# Task 9 — Virtual Environment

## What is a Virtual Environment?

A virtual environment is an isolated Python environment for a project.

It allows a project to have its own Python packages and dependencies
without affecting other Python projects on the same system.

## Why Use It?

Different projects may require different package versions.

For example:

Project A:
- Flask 2.x

Project B:
- Flask 3.x

Virtual environments keep these dependencies isolated.

## Creating a Virtual Environment

```bash
python -m venv .venv