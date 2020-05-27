import User as user
from getpass import getpass

class Login:
    def login(self):
        userName = input("Username : ")
        password = getpass("Password : ")
        
        if(Login.authentication(self,userName,password)):
            user.User(userName)

    def authentication(self, username, password):
        with open('Account.txt','r') as f:
            for line in f:
                account = line.split(";")
                if username == account[0]:
                    if password == account[1]:
                        print("Access Granted")
                        print("")
                        return True
        return False
