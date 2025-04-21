# Sorted-number-list-implementation-with-linked-lists
Step 1: Inspect the NumberListNode.py file
Inspect the class declaration for a doubly-linked list node in NumberListNode.py. The NumberListNode class has three attributes:

data: A floating-point value for the node's numerical data value
next: A reference to the next node
previous: A reference to the previous node
Getter and setter methods are provided for each attribute. NumberListNode.py is read-only since no changes are required.


Step 2: Inspect NumberList.py and SortedNumberList.py
NumberList.py contains the NumberList class definition. NumberList is a base class for a double-linked list of NumberListNodes. The list has head and tail attributes and a to_string() utility method to make a string of the list's contents from head to tail. The file is read-only since no changes are required.

SortedNumberList.py contains the SortedNumberList class definition. SortedNumberList derives from NumberList and adds insert() and remove() methods.


Step 3: Implement insert()
Implement SortedNumberList's insert() method to create a new node with the number argument as the node's data, then insert the node into the proper sorted position in the linked list. Ex: Suppose a SortedNumberList's current list is 23 → 47.25 → 86, then insert(33.5) is called. A new node with data value 33.5 is created and inserted between 23 and 47.25, thus preserving the list's sorted order and yielding: 23 → 33.5 → 47.25 → 86.


Step 4: Run code and verify output
A list of numbers named numbers_to_insert is defined near the start of the main program code in main.py. Each is inserted into a SortedNumberList, and the list is printed after each insertion. Try changing the array's content, and verify that each output is a sorted list.


Step 5: Implement remove()
Implement SortedNumberList's remove() method. The method takes an argument for the number to remove from the list. If the number does not exist in the list, the list is not changed and False is returned. Otherwise, the first instance of the number is removed from the list and True is returned.

Once remove() is implemented, change the value of the include_removals variable, defined at the start of the main program code, from False to True. Run the code and make sure that the list is correct after each removal.

Try different tests in main.py as needed, then submit code for grading. Unit tests are used to grade submitted code, so output from main.py does not affect grading.
