# Rotate a linked list to the right by k places
class linkedlist:
    def __init__(self,value):
        self.value=value
        self.next=None
node1=linkedlist(1)
node2=linkedlist(2) 
node3=linkedlist(3)
node4=linkedlist(4) 
node5=linkedlist(5)
node1.next=node2        
node2.next=node3
node3.next=node4
node4.next=node5
linkedlist.head=node1
print("Original linked list:")  
print(linkedlist.head.value)
for i in range(4):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)
def rotate(head,k):
    if not head:
        return None
    length=1
    tail=head
    while tail.next:
        tail=tail.next
        length+=1
    k=k%length
    if k==0:
        return head
    tail.next=head
    for i in range(length-k):
        tail=tail.next
        new_head=tail.next
        tail.next=None
    return new_head
k=2
rotated_head=rotate(node1,k)
print("\nRotated linked list:")
print(rotated_head.value)
for i in range(4):
    rotated_head=rotated_head.next
    print(rotated_head.value)