class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = Stack()
    print (s)
    print ("Is the stack empty: {}".format(s.is_empty()))
    s.push(3)
    s.push (7)
    s.push (5)
    print ("Elements in the stack: {}".format(s))
    s.pop()
    print ("Elements in the stack: {}".format(s))
    print ("Top of the stack element: {}".format(s.peek()))
    print ("Number of elements in the stack: {}".format(s.size()))