# Lets first declare the API

class Competitor:
    """
    A Competitor Class containing the name, Address and Email
    for each competitor.
    """

    def __init__(self, address, email):
        """

        :param address: str
        :param email: str
        """
        self._addr = address
        self._email = email

    def __eq__(self, other):
        """
        Return True iff contents of self and other are identical
        :param other: Competitor
        :return: bool
        >>> c1 = Competitor("Bob", "bob@gmail.com")
        >>> c2 = Competitor("Tim", "tim@gmail.com")
        >>> c3 = Competitor("Tim", "tim@gmail.com")
        >>> c1 == c2
        False
        >>> c2 == c3
        True
        """

        return self._addr == other._addr and self._email == other._email



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
