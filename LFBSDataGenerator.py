from random import seed
from random import random


class LFBSDataGenerator:

    # Dataset lists
    _fNames = []
    _lNames = []
    _sports = []
    _brands = []

    _idSuffix = []

    # Current user ID offset
    _curId = 0

    def __init__(self):
        self._setup()


    """
    Generate set of users in csv format, and write contents to text file.
    :param numUsers: number of users to be generated
    """
    def genUserSet(self, numUsers):
        return None


    """
    Generate a single user in csv format
    Format: id,fName,lName,address
    """
    def _genUser(self):
        return None


    def __repr__(self):
        return "I am a Lost and Found / Buy and Sell random data generator"

    """
    Perform setup for data generator
    """
    def setup(self):
