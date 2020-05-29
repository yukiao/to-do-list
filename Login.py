class Login:
    def authentication(self, username, password):
        with open('Account.txt','r') as f:
            for line in f:
                if not(line in ('\n', '\r\n')):
                    account = line.split(";")
                    if username == account[0]:
                        if password == account[1].replace('\n',''):
                            return True
        return False