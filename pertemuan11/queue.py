class QueueArray:
    def __init__(self):
        self.items = []

    def is_emtpt(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueded: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue kosong: Tidak ada elemen untuk dihapus."
        removed_item = self.items.pop(0)
        return removed_item
    
    def peel(self):
        if self.is_empty():
            return "Queue kosong"
        return self.item[0]
    
    def size(self):
        return len(self.items)
    


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None
    
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        self.count += 1
        print(f"Enqueded: {item}")

    def dequeue(self):
        if self.is_empty():
            return "Queue kosong: Tidak ada elemen untuk dihapus."
        
        temp_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        return temp_data
    
    def peek(self):
        if self.is_empty():
            return "Queue kosong"
        return self.front.data
    
    def size(self):
        return self.count