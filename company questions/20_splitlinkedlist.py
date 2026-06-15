#split linked list into k parts
class linkedlist:
    def __init__(self,value):
        self.value=value
        self.next=None  
node1=linkedlist(1)
node2=linkedlist(2)         
node3=linkedlist(3)
node4=linkedlist(4)
node5=linkedlist(5)
node6=linkedlist(6)
node7=linkedlist(7)
node8=linkedlist(8)
node9=linkedlist(9)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node9
linkedlist.head=node1
print("Original linked list:")
print(linkedlist.head.value)
for i in range(8):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)
def split(head, k):
    if not head:
        return [None]*k
    length=0
    current=head
    while current:
        current=current.next
        length+=1
    part_size=length//k
    extra_nodes=length%k
    parts=[]
    current=head
    for i in range(k):
        parts.append(current)
        current_part_size=part_size+1 if i<extra_nodes else part_size
        for j in range(current_part_size-1):
            if current:
                current=current.next
        if current:
            next_part=current.next
            current.next=None
            current=next_part
    return parts
k=3 
parts=split(linkedlist.head, k)
print("\nSplit linked list into parts:")
for i in range(k):
    print(f"Part {i+1}:")
    current=parts[i]
    while current:
        print(current.value)
        current=current.next

