from methods import method
import json
import os

class query():

    def __init__(self):
        pass

    @classmethod
    def getKey(self,key):
        pass

    @classmethod
    def getValue(self,val):
        pass

    @classmethod
    def getItems(self,key):
        pass

class db():

    name = ""

    def __init__(self,name):
        db.name = name

    @classmethod
    def cursor(self):
        return db.name

    @classmethod
    def exists(self,name):

        if (os.path.exists(name+".json")):
            return True
        else:
            return False

    @classmethod
    def create(self,name):
        data = {}
        with open(name+".json","w") as fobj:
            json.dump(data,fobj)
            fobj.close()

    @classmethod
    def delete(self,name):
        os.remove(name+".json")
