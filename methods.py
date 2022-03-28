import json




class method():

    def __init__(self):
        pass

    @classmethod
    def loadJSON(self,file) -> dict:
        with open(file,"r") as fobj:
            content = json.load(fobj)
            return content

    @classmethod
    def dumpJSON(self,data,file) -> dict:
    """
    Creates a new file so all previous data is erased, best practice is to load all data modify it and then
    dump it using this method
    """
        with open(file,"w") as fobj:
            json.dump(data,fobj,indent=6)
            fovj.close()


