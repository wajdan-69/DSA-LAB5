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

     
         
