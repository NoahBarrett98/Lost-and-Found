from random import seed
from random import random
import secrets
import os


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
    constructor to intialize the generator
    """
    def __init__(self, data_dir=None):
        self._data = read_all(data_dir)
        #generated functions with asscoiated field names
        #if we have fields that can use the same fields, this will allow us to reuse the function for that field as well
        #could just make this something we pass to object and create it in main (prob should)
        self._gen_funcs = {
             #we need to ensure uniformity between the file names, and fields of which are used to generate the tables
             USERID:_genUserId, 
             LASTNAME:_genLastName, 
             FIRSTNAME:_genFirstName
        }
       

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
    
    def read_all(self, data_dir):
         """
         reads all files in given directory
         
         returns a dict with all the read in files with the keys as their names
         """
         #if no dir is passed to function on creation
         #make empty dict
         data = {}
         if data_dir == None:
            return data
        
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
    

        

   def generate_list(self, format, n_lines):
     """
     need to establish the desired formatting for csv and sql loader
     makes a generated list .txt, based on given format which is given on class creation
     for each of the given fields it will either take from a pre-determined list or use the appropirate generation function
     format: list of relations order
     """
     f = open("generated_data.txt", "a")
     #for each user
     for c in range(0, nlines):
        line = ""
        #for each attribute in given list
        for r in format:
            #if data already exists use it, else generate new data
            try:
                #field + ", ", random selection
                line += str(data[r][random.randrange(len(data[r]))]) + ", "
             except KeyError:
                 #generate field
                line += str(_gen_funcs[r].__call__())
         f.write(line +'\n')
       f.close() 
            
            
        
        
        
        
