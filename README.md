# CSC148-SLOG
Student Learning Journal for CSC148 at the University of Toronto. Hopefully I can learn Git while I'm at it.

The SLOG Guidelines indicate that on week 3 we will have started to write our CourSe LOGS. What an apt name. So far we 
haven't covered much material and I wish there was a more complete textbook, that being said the pdf linked-to on the 
course website is a nice overview and is a good jumping-off point for further research.
I spent most of the previous class reading about Python Decorators and Closures, which seem very useful but I still 
don't have a handle on.

GitHub seems like a very interesting tool, I'm looking forward to exploring the text highlighting and version 
control structures.

``` python
print('hello GitHub!')
```

For more information about the purpose of this repository, 
visit: http://www.cdf.toronto.edu/~csc148h/winter/SLOG/slog.pdf


# Week 4 Comments:

We're learning about linked lists and how to traverse the nodes. In class, prof said that a network should contain no loops. He said that in that case the program would run endlessly. I wrote a small modification to catch those types of errors.

``` python
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
            _depth = 1              # is default (i.e. first recursion level).
            _seen = []

        if self in _seen:
            return ValueError("Infinite loop detected")
        if self.next_node is not None:
            _seen.append(self)
            return Node.end_node(self.next_node, _depth, _seen)
        else:
            return self
‘’’
While setting this up I learned that mutable objects used as default parameters are initialized at import, not when the function is called, so the default object is used across function calls. It was messing up my functions! Not a mistake I’ll make a again…

# Week 5 Notes:

Playing with sets this week, they’re very powerful. They use a hash table like a dictionary – it looks like the early set implementation is a slightly altered version of the dictionary code in the python source. This means that they're faster to check membership, since the hash table is used firsts, and the da magic methods are only used after a collision. This is much faster than using ‘a in List’.

# Week 6 Notes:

Recursion – very cool. I was playing with this in lecture. Also, working on assignment 1 was interesting, because it was difficult to get a birds-eye view of the entire simulation. I wrote a private method in our simulation as follows, which let me practice with writing to a log file directory. Using preview in Mac OS finder, I could quickly flip through the different stages of the simulation to see how the drivers and riders interacted.

``` python
def _print_status(self, step):
        """
        Print the current simulation status to file in Log folder.
        Private method used for Simulation mapping.
        @return: None
        """
        # This is a helper method for debugging, so we allow it to access private variables.
        with open('log/sim event {:0>2}.txt'.format(str(step)), 'w') as log:
            log.write("### Next Event ###\n=== Registered Drivers ===\n")
            log.writelines("\n".join(
                [str(x) for x in self._dispatcher.drivers]))
            log.write("\n\n=== driver distances ===\n")
            log.writelines("\n".join(
                self._monitor._driver_distance_breakdown()))
            log.write("\n=== Registered Riders ===\n")
            log.writelines("\n".join(
                [str(x) for x in self._dispatcher.riders]))
            log.write("\n=== events ===\n")
            log.writelines("\n".join(
                [str(x) for x in self._events._items]))
            # needs to access private list of events.
            log.write("\n\n=== monitor activities ===\n")
            log.writelines("\n".join(
                [str(x) for x in self._monitor.activity_list()]))
‘’’

The above code means that you can custom pad the variables in your string format method, for example, {:0>2} will pad the string out to two digits with zeros.


# Week 8 Notes: Binary trees

I've managed large dtsearch databases so already know a bit about how to balance search trees, but it was interesting to build basic ones from scratch. Wit will be interesting to see how to rebuild them effectively – balancing trees is complicated problem.

Week 9: Test Review

We had a test: I was surprised by how simple the questions were. Based on past exams I thought I would be more pressed for time, but I went in prepared and answered all the questions with plenty of time to spare. Checked my work and caught a few bugs. Programming by pencil is a good time?


It appears that my previous commits weren't being pushed up to the GitHub project, so I'll have to take a look at that.
In the meantime, I've learned a lot about how to merge commits and forks into the master by using GitHub to manage the private repositories for Assignments 1 and 2. They're kind enough to permit five private repositories to University students.

Our network graph lookedlike this at the end of the project:
![network graph](https://github.com/grepler/CSC148-SLOG/blob/master/Blog-Pictures/CSC146-A2%20Network%20Graph.png "Network Path")
