from abc import ABCMeta, abstractmethod

class Bank(metaclass = ABCMeta):  #create abstract class

    @abstractmethod
    def connecting(self, card, password):
        pass

class RealBank(Bank):
    def connecting(self, card, password):
        print(f'{card} is OK. connected!')

class Proxy(Bank):
    def __init__(self):
        self.bank =RealBank()
        self.__cardsInfo = [{"card": 12345678, "password": 1234, "balance": 1000}, {"card": 87654321, "password": 4321, "balance": 2000}]
        self.credentials = False
    # def appendBanned(self, bannedSite):
    #     self.__bannedList.append(bannedSite)

    def connecting(self, card, password):
        for item in self.__cardsInfo:
            if item["card"] == card and item["password"] == password:
                print('Credentials are correct!')
                self.credentials = True
                self.info = item
                break
        else:
            print('Incorrect login info!')

    def withdraw(self, amount):
        if self.credentials:
            if self.info["balance"] > amount:
                self.info["balance"] -= amount
                print(f'The process was successful. Your current balance is {self.info["balance"]}')
            else:
                print('Not enough balance!!')

class Client():
    def __init__(self):
        self.bank = Proxy()
        # self.internet.appendBanned('google.com')

    def connect(self, card, password):
        self.bank.connecting(card, password)

    def withdraw(self, amount):
        self.bank.withdraw(amount)

if __name__ == "__main__":
    print('===============================================')
    a = Client()
    a.connect(16437899, 6372)
    a.withdraw(500)
    print('===============================================')
    b = Client()
    b.connect(16437899, 1234)
    b.withdraw(500)
    print('===============================================')
    c = Client()
    c.connect(12345678, 6372)
    c.withdraw(500)
    print('===============================================')
    d = Client()
    d.connect(12345678, 1234)
    d.withdraw(1500)
    print('===============================================')
    e = Client()
    e.connect(12345678, 1234)
    e.withdraw(500)
    print('===============================================')
    f = Client()
    f.connect(87654321, 4321)
    f.withdraw(200)