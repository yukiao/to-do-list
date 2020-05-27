import Account as account
import Event as event

class User:
    def __init__(self, username):
        self.username = username
        self.path = 'User-Data/'+username+'.txt'
        User.home(self)
    
    def home(self):
        name = account.UserInfo().getAccount(self.username)
        print("Hello", name)
        choose = int(input("1. Create event\n2. View existing event\nChoose : "))
        
        if choose == 1:
            User.createEvent(self)
        elif choose == 2:
            User.viewEvents(self)
    def createEvent(self):
        eventName = input("Event name : ")
        eventPriority = input("Priority(High\Medium\Low) : ")
        eventDate = input("Date(dd/mm/yy) : ")
        event.Event(eventName,eventDate,eventPriority)

        with open(self.path,'a') as wf:
            wf.write("%s;%s;%s\n" %(eventName,eventDate,eventPriority))
    
    def viewEvents(self):
        with open(self.path,'r') as rf:
            for line in rf:
                print(line, end="")