import itertools
import sys

def sign_up():
    print("Sign up")
    username=input("Enter username: ")
    password=input("Enter password: ")
    a=username
    a=a.lower()
    while a[-1] == " ":
        a = a.replace(" ", "")
    a+="\n"
    logininfo = []
    for line in open('sample.txt'):
        separator = ':'
        line = line.split(separator)
        for value in line:
            logininfo.append(value)

    d = logininfo[::3]
    print(d)
    print(a)
    for f in d:
        if f==a:
            print("Username already taken! Try again.")
            start()

    b=password
    fw=open('sample.txt','a')
    fw.write(a)
    fw.write(b+"\n\n")
    fw.close()


    e=input("You successfully signed up! Type 'l' to log in or 'q' to quit: ")
    if e=="l":
        log_in()
    elif e=="q":
        return

    else:
        print("Try again!")
        try_again()



def log_in():
    print("Log in")
    username=input("Enter username: ")
    password=input("Enter password: ")
    a=username
    a=a.lower()
    while a[-1]==" ":
        a=a.replace(" ","")
    a+="\n"
    print(a)
    b=password
    b+="\n"
    print(b)
    logininfo = []
    for line in open('sample.txt'):
        separator = ':'
        line = line.split(separator)
        for value in line:
            logininfo.append(value)

    d = logininfo[::3]
    print(d)
    c = logininfo[1::3]
    print(c)
    for (l,k) in zip(d,c):
        if l==a and k==b:
            print("Successfully logged in!")
            sys.exit()
    print("Try again!")
    start()
def start():
    print("Do you want to sign up or log in?")
    c=input("Type 'l' to log in or 's' to sign up: ")
    if c=="l":
        log_in()
    elif c=="s":
        sign_up()
    else:
        print("Try again!")
        start()

start()




