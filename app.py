granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("User_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            grant()
            break
        file.close()
        if(success):
            print("Login Successfull!!!")
        else:
            print("Wrong username or password")

def register(name,password):
    file = open("User_details.txt","a")
    file.write("\n"+name+","+password)
    file.close()
    grant()
def access(optiom):
    global name
    if(option=="login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register ")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)

def begin():
    global option
    print("Welcome to Coding world")
    option = input("Login or Register (login,reg): ")
    if(option!="login" and option!="reg"):
        begin()
begin()
access(option)
if(granted):
    print("Welcome Congratulations, You have successfully Logged In")
    print("### User Details ###")
    print("Username: ",name)