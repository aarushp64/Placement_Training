#delete the duplicate from sorted list
class linkedlist:
    def __init__(self,value):
        self.value=value
        self.next=None
node1=linkedlist(1)
node2=linkedlist(1) 
node3=linkedlist(2)
node4=linkedlist(3) 
node5=linkedlist(3)
node1.next=node2        
node2.next=node3
node3.next=node4
node4.next=node5
linkedlist.head=node1
print("Linked list with duplicates:")
print(linkedlist.head.value)
for i in range(4):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)
def remdup(head):
    current=head
    while current and current.next:
        if current.value==current.next.value:
            current.next=current.next.next
        else:
            current=current.next
remdup(node1)
print("\nLinked list after removing duplicates:")
current = node1
while current:
    print(current.value)
    current = current.next
