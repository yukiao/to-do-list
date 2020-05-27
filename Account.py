class UserInfo:
    def __init__(self):
        self.account = {
        'sony' : 'Silverius Sony Lembang',
        'anonim' : 'Lorem'
        }
    def getAccount(self, username):
        return self.account[username]
    