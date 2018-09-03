"""Utils provided for T01 homework."""

from ast import literal_eval


def parse(string):
    """Parse a Python literal, without raising exceptions."""
    try:
        return literal_eval(string)
    except (ValueError, SyntaxError, TypeError):
        # ValueError is raised when an illegal node is in the tree
        # SyntaxError is raised when the syntax is not correct
        # TypeError is raised when a set contains a non-hashable object
        # Create an issue if you get another exception
        return None


def foreach(function, iterable):
    """Apply a function to the elements of an iterable, without returning."""
    for x in iterable:
        function(x)
