# DO NOT MODIFY THE NODE CLASS
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        # if next is None, this is the last element in the list
        self.next = next

    def __eq__(self, other):
        '''
        Understanding this function is NOT necessary for solving the problem;
        it is only used for the assertions.
        Feel free to explore your curiosity of how this works after the interview :)
        '''
        try:
            return (type(other) == Node and 
                    self.value == other.value and 
                    self.next == other.next)
        except RecursionError:
            raise Exception("Linked list has a cycle or is too large")

def not_optimal_rotate(head, k):
    if not head or k == 0:
        return head
    for i in range(k):
        prev = None
        current = head
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
            current.next = head
            head = current
    return head

def rotate(head, k):
    if not head or k == 0:
        return head

    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    old_tail = current

    k = k % length
    if k == 0:
        return head

    split_node = head
    for i in range(length - 1 - k):
        split_node = split_node.next

    new_head = split_node.next

    split_node.next = None

    old_tail.next = head

    return new_head



# Input list: a->b->c->d->e
# Rotate by 1
# Output list: e->a->b->c->d
list_1 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('e', Node('a', Node('b', Node('c', Node('d')))))
assert rotate(list_1, 1) == expected

# Input list: a->b->c->d->e
# Rotate by 2
# Output list: d->e->a->b->c
list_2 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('d', Node('e', Node('a', Node('b', Node('c')))))
assert rotate(list_2, 2) == expected

# Input list: a->b->c->d->e
# Rotate by 10
# Input list: a->b->c->d->e
list_3 = Node('a', Node('b', Node('c', Node('d', Node('e')))))
expected = Node('a', Node('b', Node('c', Node('d', Node('e')))))
assert rotate(list_3, 10) == expected

# Input list: 55->8->2->99
# Rotate by 6
# Output list: 2->99->55->8
list_4 = Node(55, Node(8, Node(2, Node(99))))
expected = Node(2, Node(99, Node(55, Node(8))))
assert rotate(list_4, 6) == expected

# Input list: 1->2
# Rotate by 5
# Output list: 2->1
list_5 = Node(1, Node(2))
expected = Node(2, Node(1))
assert rotate(list_5, 5) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
