

import stackClass
# PEP wants two lines between the import statements and the function definition.

def balanced_delimiter(string):
    """

    >>> balanced_delimiter("hell(o)")
    True
    >>> balanced_delimiter("he[l]l{(o)}")
    True
    >>> balanced_delimiter("hell(o}")
    False
    >>> balanced_delimiter("hell(o})")
    False
    >>> balanced_delimiter("hell(o})(")
    False
    >>> balanced_delimiter("hell{(o})")
    False
    >>> balanced_delimiter("{}(hello!")
    False

    :param string: str
    :return: bool
    """

    st = stackClass.Stack()

    opener_dict = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in "([{":
            st.put(char)
        elif char in ")]}" and st.isEmpty() == False:
            opener = st.remove()
            if opener != opener_dict[char]:
                return False

    return st.isEmpty()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Should start using Assert Statements or Unittest to test these functions. Could also keep using Doctest.

# For linked lists, we can create a pointer to the next Node, wherever it is. Only two Attributes.

class Node:

    def __init__(self, node_value=None, next_node=None):
        self.node_value = node_value
        self.next_node = next_node

    def __str__(self):
        return str(self.node_value)

    def end_node(self, _depth=0, _seen=0):
        """
        Recurses to the end of the node chain and returns the final Node.
        Precondition: Node chain should not be loop-linked. Will retain a list of seen id's to prevent loops.
        :param seen: lst (empty)
        :return: Node
        """

        if _depth is 0:             # I added a variable that is only 0 when the external variable
            _depth = 1              # is default (i.e. first recustion level).
            _seen = []

        if self in _seen:
            return ValueError("Infinite loop detected")
        if self.next_node is not None:
            _seen.append(self)
            return Node.end_node(self.next_node, _depth, _seen)
        else:
            return self



# Linked Lists - you an have circular collections of many Nodes joined together.

# we can now start linking nodes together.

n3 = Node("dogs")
n2 = Node("cats", n3)
n1 = Node("mice", n2)
# let's introduce a malicious link!
#n3.next_node = n1

print(n1.end_node())
# So cool thing about mutable objects defined as defaults - they define themselves at function definition time.
# So any time you re-run the same function overthe same nodes it will recognize them as being in their
# existing 'seen' dictionary.

print(n1.end_node())    # this previously evaluated as an infinite list, because the previous
                        # executable line added the Nodes to the dictionary.

# We see that it throws a ValueError (not sure what else to throw...)
# Testing started at 8:11 PM ...
# Infinite loop detected
# Process finished with exit code 0

### Linked Lists based on Sets! ###

# Lets build a linked list using a set! Won't this be fun :D

class LinkedList:
    """
    This implements the ordered list functionality using an unordered set of Node objects.
    I think that this is kinda how Python does it? (that is, that lists are actually just sets of some kind?
    Could just be hogwash."
    """

    def __init__(self, head=None):
        """
        Initialize the linked list function.
        :return:
        """
        self.entries = {}
        self.head = head
        self.count = 0

    def __str__(self):
        return self.entries

    def add(self, value):
        if self.head is 0:
            self.head = value


### End of class notes ###

# Lots of cool stuff you can do with recursion!

# Exam should be good, it's one hour long, 6-7pm next Wednesday.
# The last two hours come back to the regular lecture hall. 7:30 start.