from pymongo import MongoClient

def getDatabaseConnection():
    try:
        return MongoClient("mongodb://gh-tcbd.dyladan.me:27019")
    except Exception as e:
        print e

def getCollectionConnection(name=""):
    if not name:
        return
    try:
        db = getDatabaseConnection()
        return db[name]
    except Exception as e:
        print e