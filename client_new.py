import menu

def print_menu():
    max=menu.menu_len()
    print("Item\t\tCost")
    for i in range(1,max):
        it,ct=menu.set_menu(i)
        print(str(i)+" "+it+"\t\t"+str(ct))

def pay_ack(fl):
    if fl==1:
        print("Payment complete")
    else:
        print("Payment Failed")

def payment(cost):
    print("Select option for payment of "+str(cost))
    print('''1)Credit/Debit card
        2)Online wallet
        3)Upi''')
    ch=input(":-")
    if ch==1:
        print("You've selected Credit debit to pay "+str(cost))
        flag=1
    elif ch==2:
        print("You've selected Online wallet to pay "+str(cost))
        flag=1
    else:
        print("You've selected Upi to pay "+str(cost))
        flag=0
    pay_ack(flag)

def checkout():
    total=0
    men=[]
    print("Make basket with index")
    print_menu()
    ch=int(input("Enter choice: "))
    while ch!=99:
        ait,act=menu.set_menu(ch)
        total=total+int(act)
        men.append(ait)
        ch=int(input("Enter choice: "))
    print("Your total is : "+str(total))
    print("Your order consists of : ")
    print(men)
    payment(total)
    return men

fin=checkout()
