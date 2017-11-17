def passkey():
    usrid=input("please enter your name :")
    if usrid == "tony" or usrid == "jimmy" :
        print("hello", usrid,",,please enter your password")
        pswd = (input("****"))
        if pswd ==("tony" and "1369") or pswd == ("jimmy" and "2468"):
            print("welcome",usrid)
        else:
            print("sorry.. wrong password",usrid,'..!')
    else:
        print("sorry,, you cant enter")

passkey()