# Node class, makes code more elegant :)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Our Linked List class
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None: # same as length != 0
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node # creating a link between two Nodes 
            self.tail = new_node # setting tail as the last node in the link
        self.length += 1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0: 
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
        
        
    def get(self, index):
        if self.length == 0:
            return None
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def setValue(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.get(index)
        temp.value = value
        return temp
        
    def insert(self, index, value):
        ########## EDGE CASES ######
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        ############################
        new_node = Node(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        remembered_temp = temp.next
        temp.next = new_node
        new_node.next = remembered_temp
        self.length += 1
        return True

    def remove(self, index):
        ##### EDGE CASES #####
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        ######################
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after     = temp.next
            temp.next = before
            before    = temp
            temp      = after
    
    
    
my_ll = LinkedList(1)
my_ll.append(2)
my_ll.append(5)

my_ll.printList()