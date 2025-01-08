class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
           
        self.length += 1
    
    def pop(self):
        if self.length == 0: # no items in the list
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.tail
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
            self.length -= 1
        
        
# Driver code
if __name__ == "__main__":
    dll = DoublyLinkedList(6)
    # for i in range(1, 11):
    #     dll.append(i)
    dll.print_list()
    dll.pop()
    print("DLL After Popping Last Element")
    dll.print_list()