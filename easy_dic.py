class EasyDic:
    def __init__(self, fromDictionary={}):
        # copy fromDictionary to inner data
        self.__dict__ = fromDictionary.copy()
    def __getitem__(self, key):
        # easyDic[key] --> return value
        return self.__dict__[key]
    def __setitem__(self, key, value):
        # easyDic['key'] = value --> easyDic.key = value
        self.__dict__[key] = value
    def __repr__(self):
        return str(self.__dict__)
