import json
import os
import string
import random
import requests



headers = {
    "accept": "application/json",
    "Authorization": "User qa5xl+qHq7qObgRnrfXZoVccNYApz40TZwyKRFQ2GsM=, "
                     "Organization 05026fa75745a465c1e066d4e7cd91e3, "
                     "Element AKQF2fwr9Wrv0dtlDQZXmM2fJ3Cu9mADwtP9Kk+V55A="
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

datagencheck(10)

def flattenjson(data):
    val = dict()
    with open(datagencheck(10), "r") as f:
        data = json.load(f)
    for i in data.keys():
        if isinstance(data[i], dict):
            get = flattenjson(data[i])
            for j in get.keys():
                val[i + "." + j] = get[j]
        else:
            val[i] = data[i]
    new = set(val.keys())
    print(new)
    return new






def datafetcher(resource):
    count = 0
    api_request_url = "https://snapshot.cloud-elements.com/elements/api-v2/" + resource
    r = requests.get(api_request_url, headers=headers)
    #print(r.content)
    json_string = json.loads(r.content)[0]
    #print(json_string)
    return(json_string)

