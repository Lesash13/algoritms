class StackMax:
    def __init__(self):
        self.items = []
        self.max = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        if len(self.items) == 0:
            self.max.append(int(item))
        elif int(item) > self.max[len(self.items) - 1]:
            self.max.append(int(item))
        else:
            self.max.append(self.max[len(self.items) - 1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max.pop()
        return self.items.pop()



def get_max(self):
    if self.is_empty():
        return 'None'
    return self.max[len(self.items) - 1]


if __name__ == '__main__':
    stack = StackMax()
    command_amount = int(input())
    result = []
    for i in range(command_amount):
        command = input().split()
        if command[0] == 'push':
            stack.push(command[1])
        if command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        if command[0] == 'get_max':
            result.append(get_max(stack))
    for i in result:
        print(i)
