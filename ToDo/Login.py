class Login:
    def authentication(self, username, password):
        with open('Account.txt','r') as f:
            for line in f:
                account = line.split(";")
                if username == account[0]:
                    if password == account[1]:
                        return True
        return False