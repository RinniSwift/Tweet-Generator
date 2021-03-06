class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.lengthh = 0  # length of items in linked list
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        # running time: O(1) to check the head variable
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) to call the length variable if we have a variable that is stored that is updated in the append, prepend, and delete.
        O(n) if we node traversal through the linked list."""
        # TODO: Loop through all nodes and count one for each
        return self.lengthh

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) best and worst case if used the tail variable becasue we are just changing the tail and the next variable of the linked list without looping through it
        O(n) if we loop through the linkedlist until the end node in the case that we dont have a tail value."""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        self.lengthh += 1
        new_node = Node(item)
        tail = self.tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            tail.next = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) best and worst case because we are just changing the head variable"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        self.lengthh += 1
        node = Node(item)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) when the item is at the start or near the start of the linkedlist and we return immedietely
        TODO: Worst case running time: O(n) if the item is near the end of the linkedlist or when it is not present"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node != None:
            if quality(node.data):
                return node.data
            node = node.next
        return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) when the linked list is empty or the item to delete is in the beginnning of the linked list
        TODO: Worst case running time: O(n) when you have to traverse through the entire linked list to get to the one you want to delete or loop far into the list to delete"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        curr_node = self.head
        previous = None
        while curr_node:
            if curr_node.data == item:
                self.lengthh -= 1
                if previous:
                    if curr_node == self.tail:
                        self.tail = previous
                    previous.next = curr_node.next
                else:
                    if curr_node == self.tail:
                        self.tail = previous
                    self.head = curr_node.next
                return True
                
            previous = curr_node
            curr_node = curr_node.next

        raise ValueError('Item not found: {}'.format(item))

    def replace(self, old_item, new_item):
        '''Replace the given item with a different item
        TODO: Best case running time: O(1) where you dont have to loop through a lot of them
        TODO: Worst case runnning time O(n) where you have to loop through the entire linked list'''
        # TODO: Loop through the items in the linked list
        # TODO: Find the data you want to replace
        curr_node = self.head
        while curr_node:
            if curr_node.data == old_item:
                curr_node.data = new_item
                break
            else:
                curr_node = curr_node.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()