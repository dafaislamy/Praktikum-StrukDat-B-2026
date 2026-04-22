'''
A doubly linked list is a more complex data structure than a singly linked list,
but it offers several advantages. The main advantage of a doubly linked list is that it
allows for efficient traversal of the list in both directions.
This is because each node in the list contains a pointer to the previous node and a pointer
to the next node. This allows for quick and easy insertion and deletion of nodes from the list,
as well as efficient traversal of the list in both directions.

In a data structure, a doubly linked list is represented using nodes that have three fields:
1. Data
2. A pointer to the next node (next)
3. A pointer to the previous node (prev)
'''

class Node:
  
    def __init__(self, data):
        # To store the value or data.
        self.data = data

        # Reference to the previous node
        self.prev = None

        # Reference to the next node
        self.next = None

if __name__ == "__main__":
    # Create the first node (head of the list)
    head = Node(10)

    # Create and link the second node
    head.next = Node(20)
    head.next.prev = head

    # Create and link the third node
    head.next.next = Node(30)
    head.next.next.prev = head.next

    # Create and link the fourth node
    head.next.next.next = Node(40)
    head.next.next.next.prev = head.next.next

    # Traverse the list forward and print elements
    temp = head
    while temp is not None:
        print(temp.data, end="")
        if temp.next is not None:
            print(" <-> ", end="")
        temp = temp.next


'''
Advantages of Doubly Linked List
1. Bidirectional Traversal - You can traverse forward (using next) as well as backward (using prev).
2. Efficient Deletion - Given a pointer to a node, you can delete it in O(1) time
(no need to traverse from the head), since you can update both prev and next.
3. Insertion at Both Ends - Insertion at head or tail is efficient because
you can update both directions easily.
4. Easy to Implement Deque / Navigation Features - Useful for undo/redo,
browser history, and music playlist navigation, where both forward and
backward movement is needed.

Disadvantages of Doubly Linked List
1. Extra Memory Per Node - Each node requires an additional pointer (prev),
making DLL more memory-consuming than singly linked list.
2. More Complex Implementation - Both prev and next must be handled carefully
during insertion and deletion, which increases chances of errors (broken links, null pointer issues)
3. Slower Operations Due to Overhead - Extra pointer manipulations during
insertion/deletion cause slightly more overhead compared to singly linked list.
4. Not Cache-Friendly - Like singly linked list, nodes are scattered in memory,
so traversals may be slower compared to arrays due to poor locality of reference.
'''