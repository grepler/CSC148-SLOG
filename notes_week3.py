class Rational:
    """
    the rational class from previous lessons.
    :return:
    """

# List comprehension:
# you can use *list comprehension* to make your code shorter:


L = list(range(100))
new_list = [x * x for x in L]

# List comprehension challenges:

S = [x ** 2 for x in range(10)]
V = [2 ** x for x in range(13)]
M = [i for i in S if i % 2 == 0]
# print(S)
# print(V)
# print(M)

celsius = [39,2, 37.4, 28.2, 22]
farenheit = [(float(9)/5) * x - 32 for x in celsius]

# you need to convert to numerator to float so that you preserve the decimals
# for the conversion

colours = ['red','green','blue']
things = ['house', 'cat', 'hello']
coloured_things = ["{} {}".format(x, y) for x in colours for y in things]
print(coloured_things)


# Sieve of Eratosthenes

# generate a list of integers from 2 to 50

L = [j for i in range(2, 8) for j in range(i**2, 50, i)]
print(L)

# turns out that sets also follow comprehension syntax of a similar sort,
# so you can de-dupe in the same step

S = {j for i in range(2, 8) for j in range(i**2, 50, i)}
print(S)


# Common ADT (Abstract Data Types)
# here you want to separate the 'what' from the 'how'
# the class is the python representation of the ADT
# contains the methods and operations that can be performed on the stored data


# Recursion



class Stack:
    """
    Stack object for managing contents, last in first out (LIFO)
    """


    def __init__(self):
        """
        Initialize the Stack object.
        :return: None
        """
        self._data = []

    def isEmpty(self):
        """
        Return True is Stack contains no data.
        :return: bool
        """
        return self._data == []

    def put(self, i):
        """
        Add data to stack.
        :return: None
        """
        self._data.append(i)
        return None

    def peek(self):
        """
        Return last value of list without mutating list.
        :return: Any obj
        """
        return self._data[-1]

    def size(self):
        """
        Return length of top-level list.
        :return: int
        """
        return len(self._data)

    def remove(self):
        """
        Return and remove last entered value from data list
        :return: obj
        """
        return self._data.pop()

# checking API

s = Stack()
print("Is S Empty? ", s.isEmpty())
s.put(4)
s.put('dog')
print("Read Top Element of Stack: ", s.peek())
s.put(True)
print (s)
print("Is S Empty? ", s.isEmpty())
s.put(8.4)
print (s)
print("Remove Top Element of Stack: ",s.remove())
print("Size of Stack: ", s.size())
print("Remove One More Element from Stack: ", s.remove())
print(s)
print("Size of Stack: ", s.size())