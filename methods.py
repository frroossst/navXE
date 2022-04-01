import json

class methods():

    def __init__(self):
        pass

    @classmethod
    def loadJSON(self,file : str) -> dict:
        with open(file,"r") as fobj:
            content = json.load(fobj)
            return content

    @classmethod
    def dumpJSON(self,data,file : str) -> dict:
        """
        Best practive is to read and write all data rather than modify 
        """
        with open(file,"w") as fobj:
            json.dump(data,fobj,indent=6)
            fobj.close()


