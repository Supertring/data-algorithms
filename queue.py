# Queue data structure


class Queue:
    def __init__(self):
        self._queue = []

    # add new element to the queue
    def enqueue(self, item):
        self._queue.append(item)

    # remove the element
    def dequeue(self):
        # check if queue is empty
        if len(self._queue) < 1:
            return None
        return self._queue.pop(0)

    # display the queue
    def display(self):
        print(self._queue)

    def size(self):
        return len(self._queue)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print("No. of items inserted :", q.size())
print("Display Queue ")
q.display()
print("Dequeue the queue")
q.dequeue()
print("Display Queue ")
q.display()
print("Size of queue :", q.size())
