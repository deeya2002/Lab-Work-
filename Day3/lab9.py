# Take username and password from user and check it again for the three times whether the user has entered the right
# username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials.
username = input("Enter your username:")
password = input("Enter your password:")

for i in range(0,3):
    print("enter your credintials?")
    username1 = input("Enter your username:")
    password1 = input("Enter your password:")

    if username==username1 and password==password1:
        print("You are sucessefully logged.")
        break

    else:
        if(username!=username1 and password!=password1):
            print("Invalid Credintials")
                                          
else:
    print("3 attempt finished")