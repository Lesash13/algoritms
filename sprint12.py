class StackMax:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
       self.items.append(item)

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[0]

    def size(self):
        return len(self.items)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items[len(self.items)-1]





if __name__ == '__main__':
    s = StackMax()
    n = int(input())
    n1 = int(input())
    result = []
    for i in range(n):
        command = input().split()
        # print(command[0])
        if command[0] == 'push':
            a = s.push(command[1])
            if a == 'error':
                result.append(a)
        if command[0] == 'pop':
            result.append(s.pop())

        if command[0] == 'peek':
            result.append(s.peek())

        if command[0] == 'size':
            result.append(s.size)
    for i in result:
        print(i)
