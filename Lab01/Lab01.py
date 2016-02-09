# Lets first declare the API

class Competitor:
    """
    A Competitor Class containing the name, Address and Email
    for each competitor.
    """

    def __init__(self, name, email, address=""):
        """
        :param name: str
        :param email: str
        :param address: str
        """
        self._data = []
        self._data[0] = name
        self._data[1] = email
        self._data[2] = address

    def __eq__(self, other):
        """
        Return True iff contents of self and other are identical
        :param other: Competitor
        :return: bool
        >>> c1 = Competitor("Bob", "bob@gmail.com")
        >>> c2 = Competitor("Tim", "tim@gmail.com","Toronto")
        >>> c3 = Competitor("Tim", "tim@gmail.com","Toronto, Canada")
        >>> c1 == c2
        False
        >>> c2 == c3
        True
        """

        return self._data[0] == other._data[0] and self._data[1] == other._data[1]

    def __str__(self):
        """
        Return a string of the Competitor's information.
        :return: str
        """
        string = ""
        for item in self._data:
            string = string + ", " + item
        return string

class Runner(Competitor):
    """
    A Competitor sub-class containing information about a runner.
    """


class Registry:
    """
    A Registry Object for Competitors.
    """

    def __init__(self):
        """
        Initialize the Registry Object.
        :return: None
        :rtype: None
        """

        pass

    def add(self, runner):
        """
        add a Runner to the Registry
        :param runner:
        :type runner:
        :return: None
        :rtype: None
        """
        pass
