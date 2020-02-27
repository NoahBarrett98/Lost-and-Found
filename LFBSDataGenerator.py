from random import seed
from random import random
import secrets


class LFBSDataGenerator:

    # Datasets
    _fNames = []
    _lNames = []
    _sports = []
    _brands = []

    _idSuffix = []

    # Current user ID offset
    _curId = 0

    def __init__(self):
        self._ran = random()
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
        user = ""
        user = self._genUserId() \
               + ',' + self._genFirstName() \
               + ',' + self._genLastName()
        return user


    def _genFirstName(self):
       return secrets.choice(self._fNames)


    def _genLastName(self):
        return secrets.choice(self._lNames)


    """
    Generate a unique user ID
    """
    def _genUserId(self):
        id = secrets.choice(self._idSuffix) + self._curId
        self._curId += 1
        return str(id)



    def __repr__(self):
        return "I am a Lost and Found / Buy and Sell random data generator"


    """
    Perform setup for data generator
    """
    def _setup(self):
        self._setupIdDataset()
        self._setupFirstNameDataset()
        self._setupLastNameDataset()


    """
    Setup the ID suffix list
    """
    def _setupIdDataset(self):
        suf = 201000000
        for i in range(10):
            self._idSuffix.append(suf)
            suf += 100000


    """
    Load data set of first names into list
    """
    def _setupFirstNameDataset(self):
        # Todo: load actual data set into list
        self._fNames.append("jane")
        self._fNames.append("john")
        self._fNames.append("bob")
        self._fNames.append("lucy")
        self._fNames.append("sally") # shoutout to J.H.


    """
    Load data set of last names into list
    """
    def _setupLastNameDataset(self):
        # Todo: load actual data set into list
        self._lNames.append("dole")
        self._lNames.append("doe")
        self._lNames.append("hall")
        self._lNames.append("rupp")
        self._lNames.append("kipchoge")