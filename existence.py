'''
Given a txt file and a list of words, output the line
number of lines that have all those words(is not order sensitive).
'''

import string


def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    file_name = None
    while file_name == None:
        file_name = is_valid_file_name()
    return file_name


def is_valid_file_name():
    '''
    (str)->boolean
    checks to see if the string given corrisponds to a valid file in the directory
    '''
    file_name = None
    try:
        file_name = input("Enter the name of the file: ").strip()
        f = open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name = None
    return file_name


def remove_char(s):
    '''
    (str)->str
    takes a string and returns a copy cleaned of special characters
    '''
    for inc in [",", ".", "!", "?", ";", ":", "'", "\"", "/", "-", "_", "@", "#", "$", "%", "&", "*", ")", "("]:
        if inc in s:
            s = s.replace(inc, "")

    return s


def create_dic(l):
    '''
    (2D list)->dictonary
    returns a dictionary with unique words as keys and the lines the words appear on as values
    '''
    dic = {}
    for inc in range(len(l)):
        for l_inc in range(len(l[inc])):
            if len(l[inc][l_inc]) >= 2:
                if (l[inc][l_inc] in dic):
                    dic[l[inc][l_inc]].add(inc + 1)

                else:
                    dic[l[inc][l_inc]] = {inc + 1}

    return dic


def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    fp = open(fp).read().lower()
    fp = remove_char(fp)

    fp = fp.split("\n")
    temp = []
    for inc in range(len(fp)):
        temp.append(fp[inc].split())

    fp = temp
    del temp
    fp = create_dic(fp)
    fp = remove_num(fp)
    return fp


def remove_num(d):
    temp = []
    for ele in d:
        temp.append(ele)

    for inc in range(len(temp)):
        for l_inc in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "!", "?", ";", ":", "'", "\"", "/",
                      "-", "_", "@", "#", "$", "%", "&", "*", ")", "("]:
            x = l_inc in temp[inc]
            if l_inc in temp[inc]:
                d.pop(temp[inc])
                break

    return d


def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    query = query.split()
    found = []
    not_found = []
    return_list=[]
    if len(query) == 0:
        not_found.append("")
        return not_found

    for inc in range(len(query)):
        if query[inc] in D:
            found.append(query[inc])

        else:
            not_found.append(query[inc])
            return not_found

    co_exi = is_in(D, found)
    return_list=co_exi

    return return_list


def is_in(D, l):
    com_list=list(D[l[0]])
    for inc in range(len(l)):
        temp=list(D[l[inc]])
        counter = 0
        while counter < len(com_list):
            if com_list[counter] not in temp:
                com_list.remove(com_list[counter])
            else:
                counter=counter+1
    com_list.sort()
    return com_list


##############################
# main
##############################
file = open_file()
d = read_file(file)

flag = True
while flag:
    query = input("Enter one or more words separated by spaces, or '-q' to quit: ").strip().lower()
    if query != "-q":
        query = remove_char(query)
        res = (find_coexistance(d, query))
        if res==[]:
            print("The one or more words you entered does not coexist in a same line of the file.")

        else:
            temp = isinstance(res[0], str)
            if temp == True:
                print("The word '" + res[0] + "' is not in the file")

            else:
                temp = isinstance(res[0], str)
                if temp == True:
                    print("The word '" + res[0] + "' is not in the file")

                else:
                    new_string=str(res[0])
                    for inc in range(1, len(res)):
                        new_string = new_string + ", " + str(res[inc])
                    print("The one or more words you entered coexisted in the following lines of the file:\n" + new_string)


    else:
        flag = False

print("Goodbye")