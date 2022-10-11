import csv
import os

# find the path of the file
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
        
        
def convert_lst(name):
    lst = list(name.strip("\n").replace(" ", "").split(","))
    return lst
    

# filepath = findfile("cats.csv", "/")
# print(filepath)
bank = []
database = {}

# file_name = open(filepath, "r")
# print(file_name.readlines())
# for items in file_name:
    # info = convert_lst(items)
    # bank.append(info)

# insert to the database

# for item in bank:
#     database[item[0]] = [item[1], item[2]]


# print(database)

# file_name.close()



class Animal_Data:
    
    def __init__(self, name, age, breed, tag=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.tag = tag
        
        

choice = input("What animal are you looking for? \n")

print(os.getcwd())

try:
    with open(f"./data/{choice}.csv",newline = '') as csvfile:
        info = csv.reader(csvfile, delimiter = ',', skipinitialspace=True)
        for row in info:
         print(', '.join(row))
except Exception as e:
    print(f"Sorry, we don\'t have {choice} here.")    
    print(e)


