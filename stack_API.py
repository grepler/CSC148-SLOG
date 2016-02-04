class Stack:
    """
    Last in, First-Out (LIFO) stack
    """

    def __init__ (self):
        """
        Create a new, empty instance of Stack self
        @param Stack self: this stack
        :rtype: None
        """

        pass

    def put(self, item):
        """
        Add object obj to top of Stack self
        @param Stack self: this Stack
        @param item: Any object type
        :rtype: None
        """

        pass

    def remove(self):
        """
        Remove and return top element of Stack, if the stack is not empty.  If empty, does not return anything.
        @param Stack self: this Stack
        :rtype: Any obj
        """

        pass

    def isEmpty(self):
        """
        Return whether Stack is empty
        @param Stack self:  this Stack
        :rtype:
        """

        pass

    def peek(self):
        """
        Return top element of Stack, if the stack is not empty
        @param Stack self:  this Stack
        @rtype: Any obj
        """

        pass

    def size(self):
        """
        Return the number of element on the stack
        @param Stack self: this Stack
        :rtype: int
        """

        pass

if "__name__" == "__main__":
    import doctest
    doctest.testmod()