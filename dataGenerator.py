import json
import os
import string
import random
import requests



headers = {
    "accept": "application/json",
    "Authorization": "User , "
                     "Organization , "
                     "Element "
}

def newgen(data1):
    for key, value in data1.items():
        randomnumdata = random_num_custom()
        randomstrdata = random_string_custom(5)
        if isinstance(value, dict):
            newgen((value))
        elif isinstance(value, list):
            for v in value:
             newgen(v)
        else:
            if value in ["<<name.lastName>>", "<<name.name>>", "<<name.firstName>>", "string"]:
                data1[key] = randomstrdata
            elif str(value).find("<<random.number>>") != -1 or str(value).find("<<random.uuid>>") != -1:
                data1[key] = randomnumdata
            elif value == ".email>>":
                data1[key] = randomstrdata + ("@email.com")
            elif str(value).find("<<random.") != -1 or str(value).find("<<") != -1:
                data1[key] = randomstrdata
    return data1


def random_string_custom(n):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, n))

def random_num_custom():
    return (random.randint(1,1000))

def datagencheck(n):
    for i in range(0, n):
     with open(os.path.join(os.getcwd(),'inputfile.json'), "r") as f:
        data=json.load(f)
        for key,value in data.items():
            if isinstance(value, dict):
                newgen(value)
            elif isinstance(value, list):
                for v in value:
                    newgen(v)
            else:
              newgen(data)
        json_string = json.dumps(data)
        f=open(os.path.join(os.getcwd(),'outputfile.json'), "a+")
        if i==0:
            f.truncate(0)
            f.write("[")
            f.write(str(json_string))
        else:
            f.write(str(json_string))
        if i in range(0,n-1):
            f.write(",")
    f.write("]")
    f.close()
    print(os.path.realpath('outputfile.json'))
    return os.path.realpath('outputfile.json')

newoutputdata =datagencheck(10)

