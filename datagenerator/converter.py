import os

files_with_codes = {
    "article":[],
    "brand":[],
    "category":[],
    "device":[],
    "instrType":[]
}

def converter(files_with_codes=files_with_codes, data_dir='../datasets' ):
    converter = {}
    # iterate through entire directory
    for root, dirs, files in os.walk(data_dir):
        for i, f in enumerate(files):
            try:
                #is in file with codes?
                files_with_codes[f.split(".")[0]]
                #open file and add to converter
                f = open(data_dir+'/'+f, "r")
                for l in f.readlines():
                    l = l.split(', ')
                    converter[l[1]] = l[0]
                f.close()
            except KeyError:
                #not a conversion file
                continue
    return converter



def code_convert(code, converter=converter()):
    """
    convert a code into full val
    if using frequently pass a converter to this so we aren't recreating it everytime
    :return: full string
    """
    return converter[code]

def test():
    """
    test functions
    :return:
    """
    convert = converter()
    print("testing all codes for articles:")
    f = open("../datasets/article.txt", "r")
    for l in f.readlines():
        print(code_convert(l.split(', ')[1], convert))
    f.close()

#test()
