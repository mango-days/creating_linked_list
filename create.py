class Node :
    def __init__ ( self, data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
        
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next

llist = LinkedList()
llist.head = Node ( 1 )
llist.head.next = Node ( 2 )
llist.head.next.next = Node ( 3 )
llist.printList()