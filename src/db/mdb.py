from pymongo import MongoClient

def getDatabaseConnection():
    try:
        return MongoClient("mongodb://gh-tcbd.dyladan.me:27019")
    except Exception as e:
        print(e)

def getCollectionConnection(name=""):
    if not name or len(name)>120 or type(name) is not str:
        return
    try:
        client = MongoClient("mongodb://easySrv:serverpassword@gh-tcbd.dyladan.me:27017")
        db = client['easykey']
        return db[name]
    except Exception as e:
        print(e)