class Node:
    def __init__(self, value, next_node=None):
        # the value that the node is holding
        self.value = value
        # reference to the next node in the linked list
        self.next_value = next_node

    # method to get the value of the node
    def get_value(self):
        return self.value
    # method to get the node's next value
    def get_next(self):
        return self.next_node
    # method to update the node's next value to the input node
    def set_next(self, new_next):
        self.next_node = new_next

    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        # wrap the value in a node class and pass in the argument
        new_node = Node(value)
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            # set head and tail to new node
            self.head = new_node
            self.tail = new_node
        # otherwise, the list has at least one node
        else:
            # update the last node's next value to the new node
            self.tail.set_next(new_node)
            # update self.tail to point the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if the linked list has only one node
        if self.head == self.tail:
            # store the node we're going to remove's value
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        # otherwise, the linked list has more than one node
        else:
            # store the last node's value in another variable so we can return it
            val = self.tail.get_value()
            # start from head
            # traverse down to second last node
            current = self.head
            while current.get_next() != self.tail:
                # keep iterating
                current = current.get_next()

            # set 'self.tail' to current
            self.tail = current
            # set the new tail's next value to None
            self.tail.set_next(None)
            return val

    def remove_head(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        # check if there is only one linked list node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            # store the old head's value that we need to return
            val = self.head.get_value()
            # set 'self.head' to the old head's next value
            self.head = self.head.get_next()
            # return the old head's value
            return val