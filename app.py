import sys
from dbhelper import DBhelper
import msvcrt

def display_whole_data(data):
    hotmail=0
    gmail=0
    iiu=0
    yahoo=0
    for i in range(len(data)):
        print(f'---------------------------------{i+1}--------------------------------------')
        print('\nId : ',data[i][0],'\nname : ',data[i][1],'\nmarks : ',data[i][2],
              '\nemail : ',data[i][3])
        if  '@hotmail' in data[i][3]:
            hotmail=hotmail+1 
        elif  '@gmail' in data[i][3]:
            gmail=gmail+1 
        elif  '@iiu' in data[i][3]:
            iiu=iiu+1 
        elif  '@yahoo' in data[i][3]:
            yahoo=yahoo+1 
    return hotmail,gmail,iiu,yahoo
        
    



def get_data():
    name=input('Enter the name : ')
    email=input('Enter the email : ')
    marks=input('Enter the marks : ')
    return name,marks,email

def getch():
    return msvcrt.getch().decode()

def display_data(data):
    print('\nId : ',data[0][0],'\nname : ',data[0][1],'\nmarks : ',data[0][2],'\nemail : ',data[0][3])

class Student:
    def __init__(self):
        
        self.db=DBhelper()
        self.menu()


    def menu(self):
        print('''
                1.Register
                2.Login
                3.Delete
                4.Update
                5.Search
                6.Display whole data
                7.Exit\n
                option : 
            ''')
        option=int(getch())
        match option:
            case 1:
                self.register()
            case 2:
                self.login()
                self.loggedIn=True
            case 3:
                self.delete()
            case 4:
                self.Update()
            case 5:
                self.Search()
            case 6:
                self.Whole_data()
            case 7:
                sys.exit(1000)
            case _:
                print('----- Invalid Number -----')

    def Whole_data(self):
        data=self.db.get_all()
        print(len(data))
        h,g,i,y=display_whole_data(data=data)
        print(f'''
                Total Records : {len(data)}\n 
                hotmails={h}\n                                
                gmails={g}\n                                
                iiui emails={i}\n                                
                yahoos={y}\n                                
                                        ''')
    def register(self):
        name=input('Enter the name : ')
        email=input('Enter the email : ')
        marks=input('Enter the marks : ')
        response=self.db.register(name=name,email=email,marks=marks)
        if response:
            print("----- User Regestered Sucessfully -----")
        else:
            print("----- Error Occured -----")
        self.menu()


    def login(self):
        data=self.Search()
        if data == 1:
            print('----- Logged In ----')
        else:
            print('------ User not Found -----')
        self.menu()

    def delete(self):
        id=input('Enter ID : ')
        flag=self.db.delete(id=id)
        if flag:
            print('------Record Deleted------')
        else:
            print('------Error------')
        self.menu()
        
    def Update(self):
        id=input('Enter ID : ')
        name,marks,email=get_data()
        flag=self.db.update(name=name,marks=marks,email=email,id=id)
        if flag:
            print("------Record Updated------")
        else:
            print('------Error-----')
        self.menu()

    def Search(self):
        email=input('\nEnter email to find a Student : \n')
        data=self.db.search(email=email)
        if len(data) != 0:
            display_data(data=data)
            return 1
        else:
            return 0
   

s=Student()