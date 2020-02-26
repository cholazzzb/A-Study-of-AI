class Queue(object):
    'Queue'

    def __init__(self, build):
        self.data = [build]
        print("Stack :", self.data)

    def enqueue(self, new):
        self.data.append(new)
        print("Stack :", self.data)
    
    def dequeue(self):
        out = self.data.pop(0)
        print("Stack :", self.data)
        return out

data = Queue(5)
data.dequeue()
data.enqueue(3)
data.enqueue(23)
data.enqueue(3)
data.enqueue(234)
data.dequeue()


