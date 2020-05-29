class UserInfo:
    def __init__(self):
        self.account = {}
        self.addAccount()
    def getAccount(self, username):
        return self.account[username]
    def addAccount(self):
        with open ('UserInfo.txt','r') as rf:
            for line in rf:
                if not(line in ('\n', '\r\n')):
                    splitter = line.split(';')
                    self.account[splitter[0]] = splitter[1]