class Statuses:
    def __int__(self,id,status):
        self.__id = id
        self.__status = status

    @property
    def id(self):
        return self.__id

    @property
    def status(self):
        return self.__status