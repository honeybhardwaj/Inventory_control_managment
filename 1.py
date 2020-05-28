#importing necessary header files
import getpass
from os import system, name
from tqdm.auto import tqdm
from time import sleep
import sqlite3
import sys



#creating database
def db():
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.executescript('''
    DROP TABLE IF EXISTS admin;
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS items;
    DROP TABLE IF EXISTS bill;
    DROP TABLE IF EXISTS dealer;

    CREATE TABLE admin (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        uname TEXT UNIQUE,
        pass TEXT UNIQUE
    );
    CREATE TABLE items (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE,
        price INTEGER,
        qty INTEGER,
        dealer TEXT
    );
    CREATE TABLE bill (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        prod_id INTEGER,
        u_id INTEGER,
        status INTEGER
    );



    CREATE TABLE users (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        uname    TEXT UNIQUE,
        pass TEXT UNIQUE
    );
    ''')
    conn.commit()


#some function for designs:
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def load():
    print("\n"*2)
    print(" "*4,"LOADING.....")
    print()
    for i in tqdm(range(80)):
        print("", end="\r")
        sleep(0.025)
def drawline():
    print("_"*168)


#home is startin menu 1
def home():
    clear()
    drawline()
    print()
    print(" "*74,"LOGIN        MENU")
    drawline()
    print("\n"*2)
    print(" "*4,"LOGIN AS :")
    print(" "*4,"1.   ADMIN")
    print(" "*4,"2.   USER ")
    print()
    choice=int(input("     enter your choice:"))
    print()
    drawline()
    if choice == 1:
        load()
        admin()
    elif choice== 2:
        load()
        user()
    else:
        print("\n"*2)
        print(" "*70,"!!!!!!!  INVALID  !!!!!!!")
        home()


#admin is admin login menu:
def admin():
    clear()
    drawline()
    print()
    print(" "*74,"ADMIN        LOGIN")
    drawline()
    print("\n"*2)
    print("     ->Enter Your Credentials")
    print()
    username=input("     USERNAME:   ")
    password=getpass.getpass("     PASSWORD:   ")
    print("\n"*2)
    drawline()
    load()
    print()
    drawline()
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    command="SELECT uname, pass from admin"
    cur.execute(command)
    data=cur.fetchall()
    for i in data:
        if(username==i[0] and password==i[1]):
            access=1
            break
        access=0
    if(access==1):
        print("ACCESS GRANTED")
        amenu()
    else :
        print("\n"*2)
        print("     INVALID PASSWORD")
        admin()
    conn.commit()


#these 3 function will take care of user login menu
def user():
    clear()
    drawline()
    print()
    print(" "*74," USER        LOGIN")
    drawline()
    print("\n"*2)
    print("     1. REGISTER")
    print("     2. LOGIN")
    print()
    choice=int(input("     enter your choice:"))
    print()
    drawline()
    if choice == 1:
        load()
        signup()
    elif choice== 2:
        load()
        signin()
    else:
        print("\n"*2)
        print(" "*70,"!!!!!!!  INVALID  !!!!!!!")
        user()
def signin():
    clear()
    drawline()
    print()
    print(" "*74," LOGIN       MENU")
    drawline()
    print("\n"*2)
    print("     ->Enter Your Credentials")
    print()
    username=input("     USERNAME:   ")
    password=getpass.getpass("     PASSWORD:   ")
    print("\n"*2)
    drawline()
    load()
    print()
    drawline()
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    command="SELECT uname, pass from users"
    cur.execute(command)
    data=cur.fetchall()
    for i in data:
        if(username==i[0] and password==i[1]):
            access=1
            break
        access=0
    if(access==1):
        print("ACCESS GRANTED")
        umenu()
    else :
        print("\n"*2)
        print("     INVALID PASSWORD")
        signin()
    conn.commit()
def signup():
    clear()
    drawline()
    print()
    print(" "*74," REGISTER     MENU")
    drawline()
    print("\n"*2)
    print("     ->Enter Your Credentials")
    print()
    username=input("     USERNAME:   ")
    password=input("     PASSWORD:   ")
    print("\n"*2)
    drawline()
    print()
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('''INSERT OR IGNORE INTO users (uname, pass) VALUES ( ?, ? )''', ( username, password) )
    print("     Registered successfully.........")
    conn.commit()
    user()


#admin menu for controling
def amenu():
    clear()
    drawline()
    print()
    print(" "*74,"ADMIN        MENU")
    drawline()
    print("\n"*2)
    print("     1.ADD AN ITEM")
    print("     2.UPDATE PRICE OF AN ITEM")
    print("     3.UPDATE QUANTITY OF AN ITEM")
    print("     4.DELETE AN ITEM")
    print("     5.ITEMS OUT OF STOCK")
    print("     6.UPDATE DEALER ")
    print("     7.DISPLAY ITEM LIST")
    print("     8.EXIT")
    choice=int(input("     enter your choice:"))
    print("\n"*2)
    drawline()
    load()
    if(choice==1):
        add()
    elif(choice==2):
        uprice()
    elif(choice==3):
        uquantity()
    elif(choice==4):
        ditem()
    elif(choice==5):
        oos()
    elif(choice==6):
        dispdealer()
    elif(choice==7):
        dispitem()
    elif choice==8:
        sys.exit(0)
    else:
        print("\n"*2)
        print("     INVALID ")
    amenu()


#add an item
def add():
    clear()
    drawline()
    print()
    print(" "*74,"ADD       AN       ITEM")
    drawline()
    print("\n"*2)
    name=input("     enter product name:")
    price=int(input("     enter product price:"))
    quantity=int(input("     enter product quantity:"))
    dealer=input("     enter dealer name:")
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()

    cur.execute('''INSERT OR IGNORE INTO items (name,price,qty,dealer)
        VALUES ( ?,?,?,?)''', ( name,price,quantity,dealer ) )

    conn.commit()
    drawline()
    print("     database updated.......")
    amenu()


#update PRICE
def uprice():
    clear()
    drawline()
    print()
    print(" "*74,"UPDATE            PRICE")
    drawline()
    print("\n"*2)
    pid=int(input("     enter product id:"))
    price=int(input("     enter updated price:"))
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('UPDATE items SET price = ? WHERE id = ?',
                (price,pid))
    conn.commit()
    drawline()
    print("     database updated.......")
    amenu()


#update QUANTITY
def uquantity():
    clear()
    drawline()
    print()
    print(" "*74,"UPDATE          QUANTITY")
    drawline()
    print("\n"*2)
    pid=int(input("     enter product id:"))
    quantity=int(input("     enter updated quantity:"))
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('UPDATE items SET qty = ? WHERE id = ?',
                (quantity,pid))
    conn.commit()
    drawline()
    print("     database updated.......")
    amenu()


#delete an item
def ditem():
    clear()
    drawline()
    print()
    print(" "*74,"DELETE      AN      ITEM")
    drawline()
    print("\n"*2)
    pid=int(input("     enter product id:"))
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE from items WHERE id = ?',
                (pid,))
    conn.commit()
    drawline()
    print("     database updated.......")
    amenu()


#display OUT OF STOCK
def oos():
    clear()
    drawline()
    print()
    print(" "*59,"OUT       OF       STOCK         ITEM")
    drawline()
    print("\n"*2)
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT name from items where qty=?',
                (0,))
    a=cur.fetchall()
    print("     items that are out of stock:")
    for i in a:
        print(" "*4,i[0])
    conn.commit()
    drawline()
    if int(input("     DO You WANNA GO TO MENU:"))==1:
        amenu()


#update dealer name
def dispdealer():
    clear()
    drawline()
    print()
    print(" "*74,"UPDATE          DEALER")
    drawline()
    print("\n"*2)
    pid=int(input("     enter product id:"))
    quantity=input("     enter new product dealer:")
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('UPDATE items SET dealer = ? WHERE id = ?',
                (quantity,pid))
    conn.commit()
    drawline()
    print("     database updated.......")
    amenu()


#display items
def dispitem():
    clear()
    drawline()
    print()
    print(" "*74,"DISPLAY             ITEMS")
    drawline()
    print("\n"*2)
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute('select * from items  ')
    a=cur.fetchall()
    for i in a:
        print(" "*4,"ID:",i[0],"    name:",i[1],"   price:",i[2],"    qty: ",i[3], "   DEALER:",i[4])

    conn.commit()
    drawline()
    x=input("     DO You WANNA GO TO MENU(press 1):")
    if x =="1":
        amenu()


#user menu for its functions
def umenu():
    clear()
    drawline()
    print()
    print(" "*74,"USER         MENU")
    drawline()
    print("\n"*2)
    print("     1.BUY PRODUCT")
    print("     2.CHECKOUT ")
    print("     3.EXIT")
    choice=int(input("     Enter your choice:"))
    print("\n"*2)
    drawline()
    print()
    if(choice==1):
        buy()
    elif(choice==2):
        bill()
    elif(choice==3):
        sys.exit(0)
    else:
        print("\n"*2)
        print("     INVALID PASSWORD")
        umenu()


#helps in ordering and CHECKOUT
def buy():
    clear()
    drawline()
    print()
    print(" "*74,"PURCHASE            PRODUCT  ")
    drawline()
    print("\n"*2)

    while True :

        pid=int(input("     enter product id"))
        conn = sqlite3.connect('project.sqlite')
        cur = conn.cursor()
        cur.execute("select qty from items where id=?",(pid,))
        if(cur.fetchone()[0] > 0):
            cur.execute(' insert or ignore into bill (prod_id,status) values(?,?)',(pid,0))
            cur.execute(" update items set qty= qty - 1 where id = ?",(pid,))
        else:
            print("     item out of stock cant be added..")
        conn.commit()
        x=input("     press 0 to exit:")
        if x == '0':
            break
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    print("     enter your uresname and password to proceed")
    uname=input("     USERNAME:")
    password=getpass.getpass("     password")
    cur.execute("select id from users where uname=? and pass=?",(uname,password))
    uid=cur.fetchone()[0]
    cur.execute("update bill set u_id = ? where prod_id = ? and status= ?",(uid,pid,0))
    print("      order place please pay..")
    conn.commit()
    drawline()
    umenu()


#used for bill receipt
def bill():
    clear()
    drawline()
    print()
    print(" "*68,"         BILL                  RECEIPT")
    drawline()
    print()
    name=input("     BILLER NAME:")
    phone=input("     phone number:")
    drawline()
    load()
    clear()
    drawline()
    print()
    print(" "*68,"         BILL                  RECEIPT")
    drawline()
    print()
    print("     NAME OF BUYER:"  , name)
    drawline()
    print()
    print("     PHONE NUMBER:", phone)
    drawline()
    print("     BILL DETAILS:")
    conn = sqlite3.connect('project.sqlite')
    cur = conn.cursor()
    cur.execute(" select bill.id,bill.u_id,items.name,items.price from bill join items on bill.prod_id=items.id  where bill.status=?",(0,))
    t=cur.fetchall()
    print()
    print()
    print()
    for i in t:
        print("1.     BILL ID :",i[0],"   USER ID:", i[1], "   ITEM NAME:", i[2], "      ITEM PRICE",i[3] )
    drawline()
    total=0
    for i in t:
        total=total+i[3]
    print()
    print(" "*100,"  TOTAL AMOUNT TO BE PAID :"," "*5, total)
    drawline()
    pay=int(input("PRESS 1 TO PAY  ->"))
    drawline()
    print()
    if pay==1:
        cur.execute("update bill set status = ?",(1,))
        print(" "*68,"SHOP AGAIN THANKS")
    conn.commit()

    umenu()


home()
