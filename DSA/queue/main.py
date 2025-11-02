class Queue:
    def __init__(self, MAX, front=0, rear=0, size=0):
        self.queue = [[] for i in range(MAX)]
        self.max = MAX
        self.front = front
        self.rear = rear
        self.size = size

    def isFull(self):
        return self.size == self.max

    def isEmpty(self):
        return self.size == 0

    def add_to(self, data):
        if not self.isFull():
            self.queue[self.rear] = data
            self.rear = int((self.rear + 1) % self.max)
            self.size += 1
        else:
            print("Queue is full")

    def rem_to(self):
        if not self.isEmpty():
            print("removed value is ", self.queue[self.front])
            self.front = int((self.front + 1) % self.max)
            self.size -= 1

    def show(self):
        if not self.isEmpty():
            for i in range(self.size):
                print(self.queue[(i + self.front) % self.max])


my_queue = Queue(5)


# Another way

class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    # Pop method to remove element
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")
