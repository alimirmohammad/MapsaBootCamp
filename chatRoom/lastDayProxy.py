from abc import ABCMeta, abstractmethod

class Internet(metaclass = ABCMeta):  #create abstract class

    @abstractmethod
    def connecting(self, URL):
        pass

class RealInternet(Internet):
    def connecting(self, URL):
        print(f'{URL} is OK. connected!')

class Proxy(Internet):
    def __init__(self):
        self.internet =RealInternet()
        self.__bannedList = []

    def appendBanned(self, bannedSite):
        self.__bannedList.append(bannedSite)

    def connecting(self, URL):
        if URL in self.__bannedList:
            print('banned!')
        else:
            self.internet.connecting(URL)

class Client():
    def __init__(self):
        self.internet = Proxy()
        self.internet.appendBanned('google.com')

    def connect(self, URL):
        self.internet.connecting(URL)

if __name__ == "__main__":
    internet = Client()
    internet.connect('parsijoo.com')