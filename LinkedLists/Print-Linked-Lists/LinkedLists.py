class Node():
    '''
    Let us define a Node class which holds data of the current node and address of the next node
    Args:
        data - Data of the current node
        next -  Address of the next node
    '''

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList():
    '''
    Let us create a LinkedList class which points to a complete instance of Linked List. joining all the nodes
    '''

    def __init__(self):
        self.head = None

    def insertdata(self, data):
        '''
        Let us define a function to insert data
        '''
        node = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = node
        else:
            self.head = node

    def printList(self):
        '''
        This function is to print the LinkedList.
        '''
        temp = self.head
        while (temp.next is not None):
            print(temp.data)
            temp = temp.next
        print(temp.data)


if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.insertdata('a')
    linkedlist.insertdata('b')
    linkedlist.insertdata('c')
    linkedlist.printList()
