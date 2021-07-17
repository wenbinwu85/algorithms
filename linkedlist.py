class ListNode:
    def __init__(self, data=None, next_node=None):
        self.value = data
        self.next = next_node
        

class LinkedList:
    def __init__(self, seq):
        self.size = len(seq)
        self.head = None
        
        curr = dummy = ListNode()
        for i in seq:
            curr.next = ListNode(i)
            curr = curr.next
        
        self.head = dummy.next

    def __str__(self):
        string = ''
        curr = self.head
        while curr.next:
            string += f'{curr.value} -> '
            curr = curr.next
        string += f'{curr.value}'
        return string
        
    def get(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr
                
    def update(self, index, value):
        node = self.get(index)
        node.value = value
        
    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            prev = self.get(index-1)
            curr = self.get(index)
            prev.next = curr.next
        self.size -= 1
    
    def insert(self, index, value):
        if index == 0:
            node = ListNode(value)
            node.next = self.head
            self.head = node
        else:
            prev = self.get(index-1)
            next_node = self.get(index)
            prev.next = ListNode(value)
            prev.next.next = next_node
        self.size += 1


if __name__ == '__main__':
    data = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]

    ll = LinkedList(data)
    print(ll, ll.size)

    node = ll.get(4)
    print(node.value)
    
    ll.update(4, -1)
    print(ll, ll.size)
    
    ll.remove(4)
    print(ll, ll.size)
    
    ll.insert(4, 9)
    print(ll, ll.size)
