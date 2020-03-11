import csv
def set_menu(x):
    with open('menu.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        item=[None]*10
        price=[None]*10
        i=0
        for row in readCSV:
            item[i] = row[1]
            price[i] = row[2]
            i=i+1
        return item[x],price[x]
def menu_len():
    with open('menu.csv') as csvfile:
        readCSV = csv.reader(csvfile,delimiter=',')
        i=0
        for row in readCSV:
            i=i+1
    return i-1

#ch=int(input("Enter item index : "))
#menu(ch)
#print(menu_len())

