class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_list(self):
        current = self.head
        while current is not None :
            print(current.data)
            current = current.next

    def insert_at_end(self , value):
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

           
    def delete_value(self,value):
        if self.head is not None and self.head.data == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.data != value:
                current = current.next
            if current.next is not None:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next

if __name__ == "__main__":

    ll = Linked_list()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.delete_value(99)
    ll.delete_value(20)
    ll.insert_at_end(40)

    ll.print_list()
