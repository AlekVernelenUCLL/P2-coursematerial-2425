class Queue():
    def __init__(self):
        self.__queue = []

    @property
    def queue(self):
        return self.__queue

    def add(self, item):
        self.queue.append(item)
    
    def next(self):
        next = self.queue[0]
        self.queue.remove(next)
        return next
    
    def is_empty(self):
        return len(self.queue) == 0
    
queue = Queue()
queue.add('Alice')
queue.add('Bob')
queue.add('Charlie')

print(queue.next())
print(queue.next())
print(queue.next())