import urllib
import urllib.request
import urllib.error
import os

from functools import wraps


class BabyFetchException(Exception):
    """
    A custom exception for the cases where it fails to fetch the html file from the internet.
    """
    pass


def safe_internet_fetch(func):
    """
    (1 point)
    A decorator that catches fetching error (i.e. urllib.error.URLERROR) and raises a custom `BabyFetchException`.

    Args:
        func: The function to decorate
    Raises:
        BabyFetchException: if it fails to fetch the html codes from the url.
    """
    # TODO: Implement this decorator


@safe_internet_fetch
def fetch_top_1000(url, year):
    """
    (2 points)
    Given a year of interest, fetches the html file from the top1000 popular names
    of that year and return the html codes in text

    Args:
        url (str): The target url to send request.
        year (int): The year of interest.
    Return:
        text (str): HTML content of the fetched webpage.
    """

    # TODO: Implement this function.
    # Send POST request to the given url (https://www.ssa.gov/cgi-bin/popularnames.cgi) with the data by inspecting the web page.
    # Hint: You can concatenate multiple data using '&' (e.g. data = "month=December&day=25")
    # You must use standard library `urllib` to send request. (i.e. 3rd party libraries are not allowed.)
    # Reference link for urllib: https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen


def main():
    # NOTE: DO NOT change this function.
    # This function fetches and saves the html file of popular names in 2001-2018.
    # The html file examples are provided in `babydata/` directory.
    # The html files you generate should be identical with the provided html file examples.
    # You can check the difference with `diff` command.
    for year in range(2001, 2019):
        pathname = os.path.join("babydata", "{}.html".format(year))
        with open(pathname, "w") as f:
            url = "https://www.ssa.gov/cgi-bin/popularnames.cgi"  # target url to fetch baby data
            f.write(fetch_top_1000(url, year))


if __name__ == '__main__':
    main()
