class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None  # Queue is empty

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue size:", my_queue.size())  # Output: 3

print("Dequeue:", my_queue.dequeue())  # Output: 1

print("Is empty?", my_queue.is_empty())  # Output: False

print("Queue size:", my_queue.size())  # Output: 2
Lab qus 1
class CircularQueue:
    def _init_(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def size(self):
        if self.is_empty():
            return 0
        return (self.rear - self.front + self.capacity) % self.capacity + 1

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
        else:
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
