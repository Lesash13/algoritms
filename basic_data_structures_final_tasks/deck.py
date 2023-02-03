# ID = 81801752
from typing import List


class IsEmptyException(Exception):
    pass


class IsFullException(Exception):
    pass


class Deck:
    def __init__(self, max_size):
        self.deck_queue = [None] * max_size
        self.max = max_size
        self.size = 0
        self.head = 0
        self.tail = -1

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def is_full(self) -> bool:
        return self.size == self.max

    def push_back(self, value):
        if self.is_full:
            raise IsFullException
        else:
            self.tail = (self.tail + 1) % self.max
            self.deck_queue[self.tail] = value
            self.size += 1

    def push_front(self, value):
        if self.is_full:
            raise IsFullException
        else:
            self.head = (self.head - 1) % self.max
            self.deck_queue[self.head] = value
            self.size += 1

    def pop_back(self):
        if self.is_empty:
            raise IsEmptyException
        else:
            res = self.deck_queue[self.tail]
            self.tail = (self.tail - 1) % self.max
            self.size -= 1
            return res

    def pop_front(self):
        if self.is_empty:
            raise IsEmptyException
        else:
            res = self.deck_queue[self.head]
            self.head = (self.head + 1) % self.max
            self.size -= 1
            return res


def get_commands_output(command_amount: int, max_deck_length: int):
    deck = Deck(max_deck_length)
    for i in range(command_amount):
        command: List[str] = input().split()
        try:
            if 'pop' in command[0]:
                print(f'{getattr(deck, command[0])()}')
            else:
                getattr(deck, command[0])(command[1])
        except IsEmptyException:
            print('error')
        except IsFullException:
            print('error')


def main() -> None:
    command_amount: int = int(input())
    max_deck_length: int = int(input())
    get_commands_output(command_amount, max_deck_length)


if __name__ == '__main__':
    main()
