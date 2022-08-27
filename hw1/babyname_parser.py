#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Modified by TAs at SNU Software Platform Lab for
# SWPP fall 2022 lecture.

import sys
import re
import os

from functools import wraps

"""Baby Names exercise

Implement the babyname parser class that parses the popular names and their ranks from an html file.

1) First, you need to implement a decorator that checks whether the html file exists or not.
2) Also, the parser should extract tuples of (rank, male-name, female-name) from the html file by using regex.
   When writing regex, it's convenient to include a copy of the target text for reference.
3) Finally, you need to implement `parse` method in `BabynameParser` class that parses the extracted tuples
   with the given lambda and returns a list of processed results.
"""


class BabynameFileNotFoundException(Exception):
    """
    A custom exception for the case that the babyname file does not exist.
    """
    pass


def check_filename_existence(func):
    """
    (1 point)
    A decorator that catches the non-exiting filename argument and raises a custom `BabynameFileNotFoundException`.

    Args:
        func: The function to decorate.
    Raises:
        BabynameFileNotFoundException: if there is no such file matching the first two arguments of the function to decorate.
    """
    # TODO: Implement this decorator


class BabynameParser:

    @check_filename_existence
    def __init__(self, dirname, year):
        """
        (3 points)
        Given directory path and year, extracts the name of a file to open the corresponding file
        and a list of the (rank, male-name, female-name) tuples from the file read by using regex.
        [('1', 'Michael', 'Jessica'), ('2', 'Christopher', 'Ashley'), ....]

        Args:
            dirname (str): The name of the directory where baby name html files are stored.
            year (int): The target year to parse.
        """
        # TODO: Open and read html file of the corresponding year, and assign the content to `text`.
        # Also, make the BabynameParser to have the year attribute.
        text = "TODO"

        # TODO: Implement the tuple extracting code.
        # `self.rank_to_names_tuples` should be a list of tuples of ("rank", "male name", "female name").
        # You can process the file line-by-line, but regex on the whole text at once is even easier.
        # (If you resolve the previous TODO, the html content is saved in `text`.)
        # You may find the following method useful: `re.findall`.
        # See https://docs.python.org/3/library/re.html#re.findall.
        self.rank_to_names_tuples = [("1", "TODO_male", "TODO_female"), ("2", "TODO_male", "TODO_female")]

    def parse(self, parsing_lambda):
        """
        (2 points)
        Collects a list of babynames parsed from the (rank, male-name, female-name) tuples.
        The list must contains all results processed with the given lambda.

        Args:
            parsing_lambda: The parsing lambda.
                            It must process a single (string, string, string) tuple and return something.
        Returns:
            A list of lambda function's output
        """
        # TODO: Implement this method
