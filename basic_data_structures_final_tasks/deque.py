# ID = 81883692
from typing import List


class EmptyStackError(IndexError):
    pass


class FullStackError(IndexError):
    pass


class Deque:
    def __init__(self, max_size):
        self.__deque_queue = [None] * max_size
        self.__max = max_size
        self.__size = 0
        self.__head = 0
        self.__tail = -1

    @property
    def is_empty(self) -> bool:
        return self.__size == 0

    @property
    def is_full(self) -> bool:
        return self.__size >= self.__max

    def _inc_index(self, value) -> int:
        return (value + 1) % self.__max

    def _dec_index(self, value) -> int:
        return (value - 1) % self.__max

    def push_back(self, value):
        if self.is_full:
            raise FullStackError
        self.__tail = self._inc_index(self.__tail)
        self.__deque_queue[self.__tail] = value
        self.__size += 1

    def push_front(self, value):
        if self.is_full:
            raise FullStackError
        self.__head = self._dec_index(self.__head)
        self.__deque_queue[self.__head] = value
        self.__size += 1

    def pop_back(self):
        if self.is_empty:
            raise EmptyStackError
        res = self.__deque_queue[self.__tail]
        self.__tail = self._dec_index(self.__tail)
        self.__size -= 1
        return res

    def pop_front(self):
        if self.is_empty:
            raise EmptyStackError
        res = self.__deque_queue[self.__head]
        self.__head = self._inc_index(self.__head)
        self.__size -= 1
        return res


def call_action(deque: Deque, command) -> None:
    action = getattr(deque, command[0])
    if 'pop' in command[0]:
        print(action())
    else:
        action(command[1])


def get_commands_output(command_amount: int, max_deque_length: int):
    deque = Deque(max_deque_length)
    for _ in range(command_amount):
        command: List[str] = input().split()
        try:
            call_action(deque, command)
        except (EmptyStackError, FullStackError):
            print('error')


def main() -> None:
    command_amount: int = int(input())
    max_deque_length: int = int(input())
    get_commands_output(command_amount, max_deque_length)


if __name__ == '__main__':
    main()
