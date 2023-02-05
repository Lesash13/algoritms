# ID = 81861380
from typing import List, Any


class EmptyStackError(IndexError):
    pass


ACTIONS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}


class Stack:
    def __init__(self):
        self.__stack_list: List[Any] = []
        self.__size = 0

    @property
    def is_empty(self) -> bool:
        return self.__size == 0

    def push(self, element):
        self.__size += 1
        self.__stack_list.append(element)

    def pop(self) -> int:
        try:
            self.__size -= 1
            return self.__stack_list.pop()
        except IndexError:
            raise EmptyStackError


def calculate(values: List[str]) -> int:
    stack = Stack()
    for i in values:
        if i in ACTIONS:
            a, b = stack.pop(), stack.pop()
            stack.push(ACTIONS.get(i)(b, a))
        else:
            stack.push(int(i))

    return stack.pop()


def main() -> None:
    print(calculate(input().split()))


if __name__ == '__main__':
    main()
