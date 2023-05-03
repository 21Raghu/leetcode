
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def add_node_end(self,data):
        last = self.head
        if self.head is None:
            self.head = Node(data)
            return
        while last.next:
            last = last.next
        last.next = Node(data)
    
    def add_node_start(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_node(self):
        st = self.head
        print("print...")
        while st:
            print(st.data,"->",end='')
            st = st.next
    def pop_first(self):
        self.head = self.head.next
    
    def pop_last(self):
        if self.head is None:
            return 
        last= self.head
        while last.next.next:
            last = last.next
        last.next= None
    
    def middle_element(self):
        slow = fast = self.head
        while fast:
            slow = slow.next
            fast = fast.next.next

        print("middle element is ",slow.data)


ob = LinkedList()
ob.add_node_end(1302)
ob.add_node_end(1232)
ob.add_node_end(132)
ob.add_node_end(142)
ob.add_node_end(2)
ob.add_node_start(100)
ob.add_node_end(100)
ob.add_node_end(101)
ob.print_node()
ob.pop_last()
ob.print_node()
ob.middle_element()
