bank={}
choice=''
def RegisterUser():
    name = input("Enter the name: ")
    bank[name] = 0
def AddFunds():
    name = input("Enter the name you want to add to: ")
    amount = int(input("Enter the amount: "))
    if(name in bank):
        if(amount > 500):
            bank[name]+=amount
        else:
            print("AMount must be greater than 500")
    else:
        print("User does not exist")

def Transfer():
    source = input("Enter the name you want to transfer funds from: ")
    destination = input("Enter the name you want to transfer funds to: ")
    amount = int(input("Enter the amount: "))
    if(source and destination in bank):
        if(amount > 500):
            if(bank[source] > amount):
                bank[source] = bank[source] - amount
                bank[destination] = bank[destination] + amount
            else:
                print("Not enough balance")
        else:
            print("The amount of funds to be transferred must be greater than 500")
    else:
        print("The user does not exist!")
def Display():
    for name in bank:
        print("Name: ", name, " Balance: ", bank[name])
while(choice != 'X'):
    choice = input("Enter choice: ")
    if(choice == "A"):
        RegisterUser()
    elif(choice == "B"):
        AddFunds()
    elif(choice == "C"):
        Transfer()
    elif(choice == "D"):
        Display()