# We'll import Linked List from ../Print-Linkec-List/LinkedLists.py and
# write only the reversal function

from LinkedLists import LinkedList
import sys
sys.path.insert(1, '../Print-Linked-Lists')


class ReverseLL(LinkedList):
    '''
    Let us inherit the  LinkedList class
    '''

    def reverse(self, linkedlist):
        '''
        Funtion to reverse a linked list.
        '''
        prev = None
        curr = linkedlist.head
        while(curr is not None):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head


if __name__ == "__main__":
    linkedlist = ReverseLL()

    a = ['a', 'b', 'c']
    for item in a:
        linkedlist.insertdata(item)
    linkedlist.printList()

    linkedlist.head = linkedlist.reverse(linkedlist)
    print("**********")
    linkedlist.printList()
