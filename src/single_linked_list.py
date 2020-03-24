class Node():
    """ Node constructor """
    def __init__(self, data = None):
        """ node attributes """
        self.data = data 
        self.next = None 

class LinkedList():
    """ linked list constructor """
    def __init__(self):
        """ linked list attributes """
        self.head = Node()

    # print / display function
    def print_linked_list(self):
        # check if the head id none
        current_node = self.head 
        if (current_node.data == None):
            print(current_node.data)
        
        while (current_node):
            print(current_node.data)
            current_node = current_node.next 

    #  add start
    def add_to_start(self, start_data):
        start_node = Node(start_data)

        start_node.next = self.head
        self.head = start_node
    # add at the end
    def add_at_the_end(self, new_data):
        last_node = Node(new_data)

        # check if the head is empty
        if (self.head == None):
            self.head = last_node
            return 
        
        last_data = self.head 

        while(last_data.next):
            last_data = last_data.next 
        last_data.next = last_node

    # delete node
    def delete_node(self, value):
        # delete the first value 
        temp_head = self.head
        if (temp_head is not None and temp_head.data is value):
            self.head = temp_head.next
            temp_head = None

# tests 
new_linked_list = LinkedList()

new_linked_list.head = Node({"name": "David Kimolo"})
new_linked_list.add_to_start({"name": "Lexis newir"})
new_linked_list.add_at_the_end({"name": "last name"})
new_linked_list.add_to_start("Hello")
new_linked_list.delete_node("Hello")
new_linked_list.print_linked_list()