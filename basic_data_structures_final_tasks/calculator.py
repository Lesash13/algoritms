# ID = 81801755
from typing import List


class IsEmptyException(Exception):
    pass


actions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}


class Stack:
    def __init__(self):
        self.stack_array = []
        self.size = 0

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, element):
        self.size += 1
        self.stack_array.append(element)

    def pop(self) -> int:
        if self.is_empty:
            raise IsEmptyException
        else:
            self.size -= 1
            return self.stack_array.pop()


def calculate(values: List[str]) -> int:
    stack = Stack()
    for i in values:
        if i in actions.keys():
            a = stack.pop()
            b = stack.pop()
            stack.push(actions.get(i)(b, a))
        else:
            stack.push(int(i))

    return stack.stack_array[-1]


def main() -> None:
    print(calculate(input().split()))


if __name__ == '__main__':
    main()
