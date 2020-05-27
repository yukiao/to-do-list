import Account as account
import Event as event
import os

class User:
    def __init__(self, username):
        self.username = username
        self.path = 'User-Data/'+username+'.txt'
        User.home(self)
    
    def home(self):
        name = account.UserInfo().getAccount(self.username)
        print("Hello", name)
        choose = int(input("1. Create event \n2. View existing event \n3. Delete event \nChoose : "))
        
        if choose == 1:
            User.createEvent(self)
        elif choose == 2:
            User.viewEvents(self)
        elif choose == 3:
            User.deleteEvent(self)

    def createEvent(self):
        eventName = input("Event name : ")
        eventPriority = input("Priority(High\Medium\Low) : ")
        eventDate = input("Date(dd/mm/yy) : ")
        event.Event(eventName,eventDate,eventPriority)

        with open(self.path,'a') as wf:
            wf.write("%s;%s;%s\n" %(eventName,eventDate,eventPriority))
    
    def viewEvents(self):
        with open(self.path,'r') as rf:
            events = []
            if(os.path.getsize(self.path)>0):
                i = 1
                for line in rf:
                    events.append(line.split(";"))
                for event in events:
                    print("%d. %s" %(i,event[0]))
                    i += 1

    def deleteEvent(self):
        events = []
        with open(self.path,'r') as rf:
            if(os.path.getsize(self.path)>0):
                i = 1
                for line in rf:
                    events.append(line.split(";"))
                for event in events:
                    print("%d. %s" %(i,event[0]))
                    i += 1
            choose = int(input("Choose: "))
            print(events[choose-1][0]+" deleted")
            del events[choose-1]

            with open(self.path,'w') as wf:
                for event in events:
                    wf.write(";".join(event))
