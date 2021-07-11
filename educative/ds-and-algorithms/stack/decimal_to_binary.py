from stack import Stack

def conver_int_to_bin(dec_num: int) -> str:
    s = Stack()
    while dec_num > 0:
        remainder = dec_num % 2
        dec_num //= 2
        s.push(remainder)
    return reverse_stack(s)

def reverse_stack(s: Stack) -> str:
    result = str()
    while not s.is_empty():
        result += str(s.pop())

    return result


print(conver_int_to_bin(242))
