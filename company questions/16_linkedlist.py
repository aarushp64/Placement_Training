#create a 5 node linked list and print the values of the list one by one
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
print("Linked list:")
print(linkedlist.head.value)
for i in range(4):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)


#reverse the linked list and print the values of the list one by one
def reverse(head):
    temp=None
    while head:
        next=head.next
        head.next=temp
        temp=head
        head=next
reverse(node1)
print("\nReversed linked list:")
print(node5.value)
for i in range(4):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)




