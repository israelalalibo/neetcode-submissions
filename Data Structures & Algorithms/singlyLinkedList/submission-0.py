class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head #start at the head
        for _ in range(index): #we do not care about the iteration number
            if current is None:
                return -1
            current = current.next #point to next node

        if current is None:
            return -1
        return current.val
    

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node


    def insertTail(self, val: int) -> None:
        new_node = ListNode(val) # declare tail of list
        if self.head == None: #if linked list is empty
            self.head = new_node #make head the new node
            return

        current = self.head  #start at the head node
        while current.next is not None: # while the next node is not empty move current to next
            current = current.next 

        current.next = new_node # insert tail

    def remove(self, index: int) -> bool:
        # A->B->C->D->E 
        #iterate through 
        if self.head is None: #check to see if list is empty
            return False

        if index == 0: #to remove head
            self.head = self.head.next #make the next node the head
            return True
        
        current = self.head
        for _ in range(index - 1): #stops at the item just before the range specified
            if current.next is None:
                return False
            current = current.next

        if current.next is None:
            return False
        
        current.next = current.next.next

        return True


    def getValues(self) -> List[int]:

        values = []

        if self.head is None:
            return []

        current = self.head

        while current is not None: # while we are not at the end of the linked List
            values.append(current.val)
            current = current.next
        
        return values
