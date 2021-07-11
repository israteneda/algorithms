from stack import Stack

def reverse_string(string: str):
    stack = Stack()
    result = str()
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        result += stack.pop()

    return result

assert reverse_string("Hello") == "olleH"