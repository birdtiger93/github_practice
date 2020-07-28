class EasyDicInheritance(dict):
    def __init__(self, fromDictionary={}):
        self.update(fromDictionary)
        self.__dict__ = self
