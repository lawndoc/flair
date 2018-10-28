
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class LinkedStack(object):
    """ Link-based stack implementation."""

    def __init__(self):
        self._top = None
        self._size = 0

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        temp = Node(newItem)
        temp.setNext(self._top)
        self._top = temp
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        temp = self._top
        self._top = self._top.getNext()
        self._size -= 1
        return temp.getData()

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self._top:
            return self._top.getData()
        else:
            return None

    def replaceNext(self, new):
        if self._top:
            self.pop()
            self.push(new)

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __iter__(self):
        current = self._top
        while current:
            yield current.getData()
            current = current.getNext()

    def __str__(self):
        """Items strung from top to bottom."""
        stackStr = ""

        current = self._top
        while current != None:
            stackStr += str(current.getData()) + " "
            current = current.getNext()

        return stackStr
