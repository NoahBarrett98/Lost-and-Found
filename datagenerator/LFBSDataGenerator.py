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
    
    def read_all(self, data_dir){
         """
         reads all files in given directory
         
         returns a dict with all the read in files with the keys as their names
         """
         data = {}
         #iterate through entire directory
         for root, dirs, files in os.walk(data_dir):
            for i, f in enumerate(files):
                #if not a readable file according to load dataset, continue to next file
                try:
                    #key does not have .txt, .csv, etc
                    fsplit = f.split('.')
                    #save data set with name key 
                    data[fsplit[0]] = _loadDataset(f)
                except:
                    continue
            return data
        
    }
        
        
