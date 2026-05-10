class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copy_random_list(head):
    old_to_copy = {None: None}

    curr = head

    while curr:
        copy = Node(curr.val)
        old_to_copy[curr] = copy
        curr = curr.next

    curr = head

    while curr:
        copy = old_to_copy[curr]
        copy.next = old_to_copy[curr.next]
        copy.random = old_to_copy[curr.random]
        curr = curr.next

    return old_to_copy[head]
# Example usage:
# Given a linked list, return a deep copy of the list. Each node in the linked list contains an additional random pointer which could point to any node in the list or null.
