class Stack:
    def __init__(self) -> None:
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0
