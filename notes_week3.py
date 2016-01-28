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

