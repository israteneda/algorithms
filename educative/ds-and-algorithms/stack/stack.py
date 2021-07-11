"""
Stack Data Structure
"""
class Stack():
    def __init__(self) -> None:
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

if __name__ == "__main__":
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    print(myStack.get_stack())
    myStack.push("C")
    print(myStack.get_stack())
    myStack.pop()
    print(myStack.get_stack())
    print(myStack.is_empty())
    myStack.push("D")
    print(myStack.peek())
    anotherStack = Stack()
    print(anotherStack.is_empty())
