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



testGenMultUser(15)
