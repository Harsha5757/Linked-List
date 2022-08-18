class _Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None   # initial values
        self._tail = None
        self._size = 0

    def __len__(self):  # Built in class level method which return the size of the linked list!
       return self._size

    def isempty(self):
        return self._size == 0

    def addfirst(self, e):      # filling up the well
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def display(self):  # display method
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def addany(self, e, position): # Inserting
        newest = _Node(e, None)
        p = self._head
        i =1
        while i < position-1:
            p = p._next
            i +=1
        newest._next = p._next
        p._next = newest
        self._size = self._size+1


    def search(self, key):  # searching method
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            else:
                p = p._next
                index += 1
        return "not found!"

    def removefirst(self):
        if self.isempty():
            print("List is empty")
            return
        else:
            e = self._head._element
            self._head = self._head._next
            self._size = self._size-1
            if self.isempty():
                self._tail = None
        return e

    def removelast(self):
        if self.isempty():
            print("List is empty")
            return
        else:
            e = self._tail._element
            i = 1
            p = self._head
            while i < (self._size - 1):
                p = p._next
                i = i+1
            if self._size == 1:
                self._tail = None
                Self._head = None
            else:
                self._tail = p
                self._tail._next = None
            self._size = self._size - 1
            return f"the deleted element value is {e}"

    def removeany(self, position):
        if self.isempty():
            print("List is empty")
            return
        elif position > self._size:
            print("Given position is out of range")
            return
        else:
            p = self._head
            i = 1
            while i < position - 1:
                p = p._next
                i += 1
            if self._size == 1:
                self._head = None
                self._tail = None
            elif position == 1:
                e = p._element
                self._head = p._next
            elif position == self._size:
                e =  self._tail._element
                self._tail = p
                p._next = None
            else:
                k = p._next
                e = k._element
                p._next = k._next
            self._size = self._size - 1
        return f"the removed element is {e} "


L = LinkedList()
L.addlast(1)
L.addlast(2)
print(L._head._next._element)







