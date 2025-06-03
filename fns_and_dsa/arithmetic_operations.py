Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def perform_operation(num1: float, num2: float, operation: str):
...     operation = operation.lower()
...     
...     if operation == 'add':
...         return num1 + num2
...     elif operation == 'subtract':
...         return num1 - num2
...     elif operation == 'multiply':
...         return num1 * num2
...     elif operation == 'divide':
...         if num2 == 0:
...             return "Error: Division by zero"
...         return num1 / num2
...     else:
