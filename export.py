import json

def versionValue():
    path = "./db/botconfig.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data['version']

def prefixValue():
    path = "./db/botconfig.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data['prefix']

def tokenValue():
    path = "./db/botconfig.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data['token']

def inviteValue():
    path = "./db/botconfig.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data['inviteLink']
    
def writeUserTag(tag):
    path = "./db/botconfig.json"
    data = {}

    with open(path) as f:
        data = json.load(f)

    data['userTag'] = tag

    with open(path, 'w') as n:
        json.dump(data, n)
    
def readUserTag():
    path = "./db/botconfig.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data['userTag']

def readPlan(dayOfWeek):
    path = "./db/plan.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data[dayOfWeek]

def getNumbers(Number):
    path = "./db/lista.json"
    data = {}

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    return data[Number]