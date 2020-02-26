class Stack(object):
    'Stack'

    def __init__(self, build):
        self.data = [build]
        print("Stack :", self.data)

    def push(self, new):
        self.data.append(new)
        print("Stack :", self.data)
    
    def pop(self):
        out = self.data.pop(-1)
        print("Stack :", self.data)
        return out

data = Stack(5)
data.pop()
data.push(3)
data.push(23)
data.push(3)
data.push(234)
data.pop()

