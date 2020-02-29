import os
import random

def read_course(key, data_dir='../datasets/'):
    dept= []
    co_num = []
    co_name = []
    f = open(data_dir + '/' + key + '.txt', "r")
    for l in f.readlines():
        l = l.split(',')
        #currently have it so we are storing the codes
        dept.append(l[0])
        co_num.append(l[1])
        co_name.append(l[2])
    f.close()
    return {"dept":dept, "course_num":co_num, "course_name":co_name}


def read_w_code(key, data_dir='../datasets'):
    data = []
    f = open(data_dir + '/' + key + '.txt', "r")

    for l in f.readlines():
        l = l.split(', ')
        #currently have it so we are storing the codes
        data.append(l[1])
    f.close()

    return data



special_cases = {
    "course":read_course,
    "article":read_w_code,
    "brand":read_w_code,
    "Category":read_w_code,
    "device":read_w_code,
    "instrType":read_w_code,
}


def read_all(special_cases=special_cases, data_dir='../datasets'):
    """
    reads all files in given directory

    returns a dict with all the read in files with the keys as their names
    """
    # if no dir is passed to function on creation
    # make empty dict
    data = {}

    if data_dir == None:
        return data

    # iterate through entire directory
    for root, dirs, files in os.walk(data_dir):
        for i, f in enumerate(files):
          #check if it is in special cases
          try:
              #try to read data in using special read
              f_read = special_cases[f.split('.')[0]].__call__(f.split('.')[0])
              #handling files that have more than one field
              if isinstance(f_read, dict):

                  for k in f_read.keys():
                      data[k] = f_read[k]
              else:
                data[f.split('.')[0]] = f_read
          except KeyError:
              #not special case so read line by line:
              f_open = open(data_dir + '/' + f, "r")
              data[f.split('.')[0]] = f_open.readlines()
              f_open.close()
    return data

#use hasing of dict for this!
unique_values = {

}

def random_field(key, data):
    """
    produce random field of a given key
    :param key: field
    :param data: given data set
    :return: string field
    """
    try:
        #handle unique values error
        unique_values[key]
        #if it is a unique field pop it from the list
        return data[key].pop([random.randrange(len(data[key]))])
    except KeyError:
        #if not just return a regular field
        return data[key][random.randrange(len(data[key]))]

def random_field_t():
    data = read_all()
    for i in range(0, 10):
        print(random_field('dept', data))

#random_field_t()

def read_all_t():
    """
    test
    :return:
    """
    print("reading all files")
    data = read_all()
    for k in data.keys():
        for val in data[k]:
            print(val)

