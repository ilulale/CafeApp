import menu

def print_menu():
    max=menu.menu_len()
    print("Item\t\tCost")
    for i in range(1,max):
        it,ct=menu.set_menu(i)
        print(str(i)+" "+it+"\t\t"+str(ct))

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

checkout()