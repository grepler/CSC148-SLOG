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

        self._list = []

    def put(self, item):
        """
        Add object obj to top of Stack self
        @param Stack self: this Stack
        @param item: Any object type
        :rtype: None
        """

        self._list.append(item)

    def remove(self):
        """
        Remove and return top element of Stack, if the stack is not empty.  If empty, does not return anything.
        @param Stack self: this Stack
        :rtype: Any obj
        """

        if len(self._list) > 0:
            return self._list.pop()

    def isEmpty(self):
        """
        Return whether Stack is empty
        @param Stack self:  this Stack
        :rtype: bool
        """

        return len(self._list)  == 0

    def peek(self):
        """
        Return top element of Stack, if the stack is not empty
        @param Stack self:  this Stack
        :rtype: Any obj
        """

        if len(self._list) > 0:
            return self._list[-1]

    def size(self):
        """
        Return the number of element on the stack
        @param Stack self: this Stack
        :rtype: int
        """

        return len(self._list)

    def __str__ (self):
        """
        Print element of the Stack
        :rtype: str
        """
        copySelf = self._list[:]
        return ", ".join(str(eachElement) for eachElement in copySelf)