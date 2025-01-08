class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    def find_middle_node(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            return self.head
            
        slow_ptr = self.head
        fast_ptr = self.head
        
        # Traversal logic
        while fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next # double jump
            temp_checker = fast_ptr.next
            
            if temp_checker is None:
                return slow_ptr
            if temp_checker.next is None:
                return slow_ptr.next

        return slow_ptr
        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""