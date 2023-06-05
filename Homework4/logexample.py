from logging import debug, info, warning, error, critical, basicConfig, DEBUG
class Logging:
    def __init__(self, message = ""):
        self.Message = message
    def __str__(self):
        if(self.Message == "" or self.Message == None):
            raise TypeError("Value cann't be None or empty!")
        return self.Message
    def BasicConfig(self, level):
        fileName = "filelog.log"
        format = "%(asctime)s : %(levelname)s - %(message)s"
        basicConfig(level=level, filename=fileName, format=format, filemode='a')
    def Log(self, levelType = 0):
        if(levelType == 0):
            debug(self.__str__())
        elif(levelType == 1):
            info(self.__str__())
        elif(levelType == 2):
            warning(self.__str__())
        elif (levelType == 3):
            error(self.__str__())
        elif(levelType == 4):
            critical(self.__str__())