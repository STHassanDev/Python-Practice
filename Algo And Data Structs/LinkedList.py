# While python lists are good at accessing and reading, Linked Lists are good at 
# inserting

class Node:
    # An object for storing a single node of a linked list. 
    # Contains data and a pointer to the next node.

    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data

class LinkedList:

    # Singly Linked List

    def __init__(self):
        self.head = None

    def __repr__(self) -> str: #Takes O(n) time
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next
        return  '-> '.join(nodes)

    def is_empty(self): #Takes O(1) time
        return self.head == None

    def size(self): #Takes O(n) time
        # Returns the number of nodes in the list. O(n)
        curent=self.head
        count=0

        while curent:
            count+=1
            curent=curent.next 

        return count

    def add(self,data): #Takes O(1) time
        # Add new node at the head of the list 
        # O(1)

        new=Node(data)
        new.next=self.head
        self.head=new

    def search(self, key): #Takes O(n) time
        # Search for the first node containing data that matches the key
        # O(n) 

        current=self.head

        while current:
            if current.data ==key:
                return current
            else:
                current=current.next
        return  None

    def insert(self,data,index): #Takes O(n) time
        # Inserts a new node at index position 
        # Inserting is constant time but finding the node at the index takes O(n)
        if index==0:
            self.add(data)
        elif index>0:
            new=Node(data)
            
            pos=index
            current=self.head

            while pos>1:
                current=current.next
                pos-=1
            
            new.next=current.next
            current.next=new

    def remove(self,key): #Takes O(n) time
        current=self.head
        prev=None
        found=False

        while current and not found:
            if current.data==key and current is self.head: 
                found = True
                self.head=current.next
                return current
            elif current.data==key:
                found=True
                prev.next=current.next
                return current
            else:
                prev=current
                current = current.next
        return None

    def delete(self,index): #Takes O(n) time
        if index==0:
            self.head=self.head.next
            return self.head

        elif index>0:
            pos=index
            current=self.head

            while pos>1:
                current=current.next
                pos-=1
            
            prev = current
            current = current.next
            next = current.next

            prev.next = next

            return current
