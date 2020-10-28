class Queue:
    def __init__(self):
        self.items = []

    def enque(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    queue.enque('Hello')
    queue.enque('hi')
    queue.deque()
    print(queue.size())
