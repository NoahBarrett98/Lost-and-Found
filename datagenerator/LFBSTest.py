from LFBSDataGenerator import LFBSDataGenerator as gen


# Generate single user
def testGenUser():
    generator = gen()
    user = generator._genUser()
    print(user)


def testGenMultUser(numUsers):
    generator = gen()
    for i in range(numUsers):
        user = generator._genUser()
        print(user)


def testLoadDataSetFNames():
    generator = gen()
    # load first names into first name list
    generator.loadFirstNameDataset("first_names.txt")
    for name in generator._fNames:
        print(name)



""" UNCOMMENT LINE TO RUN TEST """

# testGenMultUser(15)
testLoadDataSetFNames()
