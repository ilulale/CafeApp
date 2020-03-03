
def options():
    print("""\tMenu
    \t1)Show orders
    \t2)Complete order
    \t3)Exit""")
    ch=0
    while int(ch)!=3:
        ch=input("Enter your choice ")
        if int(ch)==1:
            #print all the orders
            print_order()
        elif int(ch)==2:
            print("Complete ")

def print_order():
    id = open("clientiddb.txt","r")
    id = id.readlines()
    tok = open("tokendb.txt","r")
    tok = tok.readlines()
    x = len(id)
    print("Token \t Id")
    for i in range(x):
        print(tok[i]+"\t"+id[i])
print("Welcome to the server")
#options()
print_order()