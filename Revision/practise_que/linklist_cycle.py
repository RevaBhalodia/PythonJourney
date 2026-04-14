class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Example creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = head.next  # cycle

print("Cycle present:", has_cycle(head))