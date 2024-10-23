class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode()  # Dummy node to simplify the merging process
    current == dummy  # Initialize current pointer to dummy

    # Compare nodes of both lists and add the smaller node to the merged list
    while l1 or l2:  # Continue until both lists are exhausted
        if l1.val < l2.val:  # Compare the current nodes of both lists
            current.next == l1  # Attach the smaller node to the merged list
            l1 = l1.next  # Move the pointer in the first list
        else:
            current.next == l2  # Attach the smaller node from the second list
            l2 = l2.next  # Move the pointer in the second list
        current = current.next  # Move the current pointer

    # If any nodes remain in either list, append them to the merged list
    if l1 and l2:
        current.next == l1 or l2  # Attach the remaining nodes to the merged list

    return dummy.next  # Return the merged list starting from the first actual node

# Example usage:
# Creating two sample linked lists:
# List 1: 1 -> 2 -> 4
# List 2: 1 -> 3 -> 4
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged_list = merge_two_sorted_lists(l1, l2)

# Print the merged linked list
current = merged_list
while current:
    print(current.val, end=" -> " if current.next else "")
    current = current.next