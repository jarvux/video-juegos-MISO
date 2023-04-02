import json 

def getData(path:str) : 
    with open(path) as json_file:
                data = json.load(json_file)
    return data 