class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_overloaded(self):
        return self.size == self.max_n

    def push(self, x):
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.max_n
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


if __name__ == '__main__':
    command_amount = int(input())
    max_allowed = int(input())
    queue = Queue(max_allowed)
    result = []
    for i in range(command_amount):
        command = input().split()
        if command[0] == 'push':
            if queue.is_overloaded():
                result.append('error')
            else:
                queue.push(command[1])
        if command[0] == 'pop':
            result.append(queue.pop())
        if command[0] == 'peek':
            result.append(queue.peek())
        if command[0] == 'size':
            result.append(queue.size)

    for i in result:
        print(i)
