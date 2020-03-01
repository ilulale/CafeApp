import requests as req
def client_init():
    f = open("clientiddb.txt","r")
    check=f.read()
    id=1
    for i in check: 
        if (i==check):
            continue
        else:
            id=i
    f.close
    f = open("clientiddb.txt","a")
    id=int(id)
    id=id+1
    id=str(id)
    f.write("\n"+id)
    print("New id assinged:- "+id)
    f.close
    return id

def menu():
    total=0
    order=["Order"]
    print("""\n \tWelcome to the Cafeteria
        \t1)Breakfast
        \t2)Lunch
        \t3)Beverages""")
    choice=int(input("Choice "))
    if(choice==1):
        print("""\n\t Breakfast Menu
        \t 1)Wada pav
        \t 2)Samosa
        \t 3)Missal Pav
        \t 4)Bread Pakoda
        \t 5)Bhurji pav
        \t 6)Omlette
        \t 7)Poha
        \t 99)Exit and Tally""")
        bkc=int(input("Enter your oder"))
        while bkc!=99:
            if bkc==1 or bkc==2 or bkc==3:
                total=total+12
                if bkc==1:
                    order.append("Wadapav")
                elif bkc==2:
                    order.append("Samosa")
                else:
                    order.append("Missal Pav")
            elif bkc==4 or bkc==6 or bkc==7:
                total=total+20
                if bkc==4:
                    order.append("Bread Pakoda")
                elif bkc==6:
                    order.append("Omlette")
                else:
                    order.append("Poha")
            elif bkc==5:
                total=total+15
                order.append("Bhurji Pav")
            bkc=int(input("Want to addon? "))
    elif (choice==2):
        print("Lunch")
        #copy code for lunch from breakfast
    else:
        print("Beverages")
        #copy code for beverages from breakfast
    print("\tThe order is")
    for x in order:
        print("\t"+x)
    return total

def payment(tot):
    resp = req.get("https://github.com/ilulale/CafeAppn")
    if resp.status_code==200:
        return 1
    else:
        return 0    

def token_gen(num):
    g=open("tokendb.txt","r")
    check=g.read()
    num=int(num)
    i=num+1
    tok=1
    for i in check:
        if(i==check):
            continue
    else:
        tok=i
    g.close()
    g = open("tokendb.txt",'a')
    tok=int(tok)
    tok=tok+1
    g.write("\n"+str(tok))
    print("Your order token is:- "+str(tok))
    g.close
    return tok


print("Welcome")    
cid=client_init()
total=menu()
print("The total is INR/- "+str(total))
pay=payment(total)
if pay==1:
    print("Payment done")
    token=token_gen(cid)
else:
    print("Payment unsuccessful, try again")