#merging two linked lists

class linkedlist:
    def __init__(self, value):
        self.value = value
        self.next = None
list1 = linkedlist(1)
node6 = linkedlist(3)
node7 = linkedlist(5)
list1.next = node6
node6.next = node7
list2 = linkedlist(2)
node8=linkedlist(4)
node9=linkedlist(6)
node8=linkedlist(4)
node9=linkedlist(6)
list2.next=node8
list2.next.next=node9
linkedlist.head=list1
print("Linked list 1:")
print(linkedlist.head.value)
for i in range(2):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)    
linkedlist.head=list2
print("\nLinked list 2:")
print(linkedlist.head.value)    
for i in range(2):
    linkedlist.head=linkedlist.head.next
    print(linkedlist.head.value)

def merge(list1, list2):
    dummy = linkedlist(0)
    temp = dummy
    while list1 and list2:
        if list1.value < list2.value:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
        temp = temp.next
    if list1:
        temp.next = list1
    else:
        temp.next = list2
    return dummy.next
print("\nMerged linked list:")
merged = merge(list1, list2)
current = merged
while current:
    print(current.value)
    current = current.next

#