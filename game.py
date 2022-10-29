##this is the password storing thing 

main_question = input("What is the master password? ")
main_password = "x"

def view():
    with open('shit.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, psw = data.split('|')
            print("Account:", user, "| Password:", psw)

def add():
    account = input("Account: ")
    passwords = input("Password: ")
    with open('shit.txt', 'a') as f:
        f.write(account + '|' + passwords + '\n')

while True:

    if main_question == main_password:
        view_or_add = input("Do you want to view or add new password? (view/add), press q to quit. ").lower()

        if view_or_add == "view":
            view()    
        elif view_or_add == "add":
            add()
        elif view_or_add == "q":
            break
    else:
        print("Incorrect Password Please try again!")
        







