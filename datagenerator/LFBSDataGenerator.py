from random import seed
from random import random
import read_files
import converter
import secrets
import numpy as np

class LFBSDataGenerator:
    # Datasets
    _fNames = []
    _lNames = []
    _sports = []
    _brands = []
    _idSuffix = []

    _data = read_files.read_all()
    # Current user ID offset
    _curId = 0


    """
    Generate set of users in csv format, and write contents to text file.
    
    Args:
        numUsers (int) : number of users to be generated
    """
    def genUserSet(self, numUsers):
        # Todo: create users and write to text file
        return None

    """
    Setup the ID suffix list
    """
    def loadIdDataset(self):
        # todo : load actual id's from text file
        suf = 201000000
        for i in range(10):
            self._idSuffix.append(suf)
            suf += 100000

    """
    Load data set of first names into list
    """
    def loadFirstNameDataset(self, fileName):
        self._fNames = self._loadDataset(fileName)

    """
    Load data set of last names into list
    """
    def loadLastNameDataset(self):
        # Todo: load actual data set into list (see loadFirstNameDataset)
        self._lNames.append("dole")
        self._lNames.append("doe")
        self._lNames.append("hall")
        self._lNames.append("rupp")
        self._lNames.append("kipchoge")

    """
    Generate a single user in csv format
    
    Returns:
        user (str) : id,fName,lName,address
    """
    def _genUser(self):
        user = self._genUserId() \
               + ',' + self._genFirstName() \
               + ',' + self._genLastName()
        return user

    """
    Randomly choose and return a first name from list
    """
    def _genFirstName(self):
       return secrets.choice(self._fNames)
    """
    Randomly choose and return a list name from list
    """
    def _genLastName(self):
        return secrets.choice(self._lNames)

    """
    Generate a unique user ID
    """
    def _genUserId(self):
        id = secrets.choice(self._idSuffix) + self._curId
        self._curId += 1
        return str(id)

    """
    Return string
    """
    def __repr__(self):
        return "I am a Lost and Found / Buy and Sell random data generator"

    """
    Loads dataset from text file into list
    
    Args:
        fileName (str) : name of dataset file
        
    Returns:
        list[str] : list of separated entries
    """
    def _loadDataset(self, fileName):
        file = open(fileName, 'r')
        # dsList = file.readlines()
        dsList = file.read().splitlines()
        file.close()
        return dsList

    items = {
        # True = not unique, False = unique
        'datePosted': [8, True, "d"],
        'dateRecieved': [8, True, "d"],
        'dateShipped': [8, True, "d"],
        'ISBN': [13, False],
        'itemID': [7, False],
        'listPrice': [5, True],
        'recyclerID': [7, False],
        'recyclerNumber': [10, False],
        'serialNo': [30, False],
        'transDate': [8, True, "d"],
        'year': [4, True, "y"]
    }

    def generate_numeric_field(field, length, items=items):

        data = []
        try:
            if items[field][2] == "d":
                yr = [i for i in range(2000, 2020)]
                day = [i for i in range(1, 31)]
                mn = [i for i in range(1, 12)]
                for i in range(0, length):
                    concat = [str(np.random.choice(day)), str(np.random.choice(mn)), str(np.random.choice(yr))]
                    for i in concat:
                        if len(i) == 1:
                            concat[int(i)] = '0'+i
                    data.append(str())
            elif items[field][2] == "y":
                dates = [i for i in range(2000, 2020)]
                for i in range(0, length):
                    np.random.choice(dates)

        except IndexError:
            #if can repeat
            if items[field][1]:
                for i in range(0, length):
                    val = np.random.permutation(items[field][0])
                    val = [str(c) for c in val]
                    data.append(''.join(val))
            else:
                 for i in range(0, length):
                    s = ''
                    num_z = items[field][0] - len(str(i))
                    s += '0'*num_z
                    s+=i
                    data.append(s)
        return data

    print(generate_numeric_field(field='datePosted', length=5))

    _gen_funcs = {
        'datePosted': generate_numeric_field,
        'dateRecieved': generate_numeric_field,
        'dateShipped': generate_numeric_field,
        'ISBN': generate_numeric_field,
        'itemID': generate_numeric_field,
        'listPrice': generate_numeric_field,
        'recyclerID': generate_numeric_field,
        'recyclerNumber': generate_numeric_field,
        'serialNo': generate_numeric_field,
        'transDate': generate_numeric_field,
        'year': generate_numeric_field
    }

    def generate_list(self, format, n_lines, fname, _gen_funcs=_gen_funcs, _data=_data):
        """
        need to establish the desired formatting for csv and sql loader
        makes a generated list .txt, based on given format which is given on class creation
        for each of the given fields it will either take from a pre-determined list or use the appropirate generation function
        format: list of relations order
        """
        f = open(fname, "a")
        # for each user
        for c in range(0, n_lines):
            line = ""
            # for each attribute in given list
            for r in format:
                # if data already exists use it, else generate new data
                try:
                    # field + ", ", random selection
                    line += read_files.random_field(_data[r], _data) + ", "
                except KeyError:
                    # generate field
                    line += str(_gen_funcs[r].__call__(r, n_lines))
            f.write(line + '\n')
        f.close()
