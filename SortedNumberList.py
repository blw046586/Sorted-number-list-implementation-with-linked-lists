# SortedNumberList.py

# Import the necessary base classes
# Ensure these files exist and are correctly named/imported
from NumberListNode import NumberListNode
from NumberList import NumberList

class SortedNumberList(NumberList):
    """
    A doubly linked list that maintains nodes in ascending sorted order
    based on the node's data value. Inherits from NumberList.
    """
    def __init__(self):
        """Initializes an empty sorted number list."""
        super().__init__() # Initialize head and tail from base class (sets them to None)

    def insert(self, number):
        """
        Creates a new node with the given number and inserts it into the
        list, maintaining sorted order.
        """
        new_node = NumberListNode(number) # Create the node to insert

        # Case 1: The list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        # Case 2: Insert before the current head
        if new_node.get_data() <= self.head.get_data():
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node # New node is the new head
            return

        # Case 3: Insert in the middle or at the tail
        # Find the node *before* the insertion point
        current_node = self.head
        while current_node.get_next() is not None and \
              new_node.get_data() > current_node.get_next().get_data():
            current_node = current_node.get_next()

        # At this point, current_node is either the node just before
        # where new_node should go, or current_node is the tail.

        if current_node.get_next() is None:
            # Insert after the current tail
            current_node.set_next(new_node)
            new_node.set_previous(current_node)
            self.tail = new_node # New node is the new tail
        else:
            # Insert in the middle: between current_node and next_node
            next_node = current_node.get_next()
            new_node.set_next(next_node)
            new_node.set_previous(current_node)
            current_node.set_next(new_node)
            next_node.set_previous(new_node)

    def remove(self, number):
        """
        Removes the first node found containing the specified number.
        Returns True if the number was found and removed, False otherwise.
        """
        current_node = self.head

        # Iterate through the list looking for the number
        while current_node is not None:
            # Optimization: If we pass the point where the number should be,
            # it's not in the list (because the list is sorted).
            if current_node.get_data() > number:
                return False

            if current_node.get_data() == number:
                # Found the node to remove
                prev_node = current_node.get_previous()
                next_node = current_node.get_next()

                # Update pointers based on node's position
                if prev_node is None and next_node is None:
                    # Case: Removing the only node in the list
                    self.head = None
                    self.tail = None
                elif prev_node is None:
                    # Case: Removing the head node (list has >= 2 nodes initially)
                    self.head = next_node
                    next_node.set_previous(None) # New head's previous is None
                elif next_node is None:
                    # Case: Removing the tail node (list has >= 2 nodes initially)
                    self.tail = prev_node
                    prev_node.set_next(None) # New tail's next is None
                else:
                    # Case: Removing a middle node
                    prev_node.set_next(next_node)
                    next_node.set_previous(prev_node)

                # Node was found and removed
                return True

            # Move to the next node
            current_node = current_node.get_next()

        # If the loop completes, the number was not found
        return False

# Reminder: Ensure you have correctly defined NumberListNode.py and NumberList.py
# including a functional to_string() method in NumberList for printing.
# Example base NumberList (ensure yours is similar):
# class NumberList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def get_head(self): return self.head
#     def get_tail(self): return self.tail
#
#     def to_string(self, separator=", ", open_paren="(", close_paren=")") -> str:
#         """ Creates a string representation like (item1, item2, item3) """
#         result = []
#         node = self.head
#         while node:
#             result.append(f"{node.get_data():.2f}") # Format to 2 decimal places
#             node = node.get_next()
#         if not result:
#             return "(empty)"
#         return open_paren + separator.join(result) + close_paren
