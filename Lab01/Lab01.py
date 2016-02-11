# Lets first declare the API

class Competitor:
    """
    A Competitor Class containing the name, Address and Email
    for each competitor.
    """

    def __init__(self, name, email, address) -> object:
        """
        :param name: str
        :param email: str
        :param address: str
        """
        self._data = []
        self._data.append(name)
        self._data.append(email)
        self._data.append(address)

    def __eq__(self, other):
        """
        Return True iff contents of self and other are identical
        :param other: Competitor
        :return: bool
        >>> c1 = Competitor("Bob", "bob@gmail.com", "New York")
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
        >>> c1 = Competitor("Bob", "bob@gmail.com", "Georgetown")
        >>> c2 = Competitor("Tim", "tim@gmail.com","Toronto")
        >>> c3 = Competitor("Tim", "tim@gmail.com","Toronto, Canada")
        >>> print(c1)
        Bob, bob@gmail.com
        >>> print(c2)
        Tim, tim@gmail.com
        """
        string = self._data[0] + ", " + self._data[1]
        return string

class Runner(Competitor):
    """
    A Competitor sub-class containing information about a runner.

    ### Private Attributes ###
    @type _data: list
        item consists of name, email, address, time, category
    """

    def __init__(self,name, email, address, time):
        """
        initilizes a Runner type competitor and tracks time and category.
        :param name: str
        :param email: str
        :param address: str
        :param time: float
        """
        super().__init__(self, name, email, address)
        self._data.append(address)
        self._data.append(time)
        self._data.append(self.categorize_runner())

    def categorize_runner(self):
        """
        based on runner time, separate into categories
        :return: None
        """
        if self._data[3] > 40.0:
            return "Very Slow"
        elif self._data[3] > 30.0:
             return "Slow"
        elif self._data[3] > 20.0:
            return "Moderate"
        elif self._data[3] > 10.0:
            return "Fast"
        elif self._data[3] <= 10.0:
            return "Hyperspeed"

class Registry:
    """
    A Registry Object for Competitors.

    >>> r = Registry()
    >>> r.add(Runner("Bob", "bob@gmail.com", "Georgetown",8.0)))
    >>> r.category("Hyperspeed")
    Bob, bob@gmail.com

    """

    def __init__(self):
        """
        Initialize the Registry Object.
        :return: None
        :rtype: None
        """

        self._register = []

    def add(self, runner):
        """
        add a Runner to the Registry
        :param runner:
        :type runner:
        :return: None
        :rtype: None

        >>> r = Registry()
        >>> r.add(Runner("Bob", "bob@gmail.com", "Georgetown",8.0)))
        >>> r.add(Runner("Gwen", "Gwen@gmail.com", "Georgetown",12.0)))
        >>> r.add(Runner("Bob", "bob@gmail.com", "New York",12.0)))
        ValueError - already registered
        """

        if runner not in self._registry:
            self._register.append(runner)
        else:
            TypeError("Runner already in Registry")


    def remove(self, name, email):
        """
        Remove runner from registry.
        :param runner: str
            email address of runner
        :return: None
        >>> r = Registry()
        >>> r.add(Runner("Bob", "bob@gmail.com", "Georgetown",8.0)))
        >>> r.add(Runner("Gwen", "Gwen@gmail.com", "Georgetown",12.0)))
        >>> r.add(Runner("Bob", "bob@gmail.com", "New York",12.0)))
        >>> r.remove(self, "Bob", "bob@gmail.com")
        """
        pass

    def category(self, group):
        """
        Return category listing
        :param group: str
        :return: str
        """