class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, x):
        self.queue.append(x)

    def get(self):
        if self.is_empty():
            return 'error'
        else:
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)


if __name__ == '__main__':
    command_amount = int(input())
    queue = Queue()
    result = []
    for i in range(command_amount):
        command = input().split()
        if command[0] == 'put':
            queue.put(command[1])
        if command[0] == 'get':
            result.append(queue.get())
        if command[0] == 'size':
            result.append(queue.size())

    for i in result:
        print(i)
