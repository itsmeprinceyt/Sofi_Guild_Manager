from cryptography.fernet import Fernet
class KEYHOLDER:
    @classmethod
    def set_key(cls,k):
        cls.KEY=k
class guild:
    name=""
    elixir=0
    temp=0
    wist=0
    withdraw=0
    def __init__(self,n,e,w,wd):
        '''This runs when the objects are made, this is only for first time usage'''
        self.name=n
        self.elixir=e
        self.wist=w
        self.withdraw=wd
    def set_data(self,n,e,w,wd):
        '''This will be used to get latest data after withdrawing'''
        self.name=n
        self.elixir=e
        self.wist=w
        self.withdraw=wd
    def elixir_update(self,Uelixir):
        '''This will update elixir of every account'''
        self.elixir+=Uelixir
        self.temp=self.elixir
        self.wist=0
        while self.temp>=600:
            self.temp-=600
            self.wist+=1
    def BLelixir_update(self):
        '''This is made for blacklisted users so they won't get any elixir since they are banned'''
        self.temp=self.elixir
        self.wist=0
        while self.temp>=600:
            self.temp-=600
            self.wist+=1
    def elixir_withdraw(self,Welixir):
        '''This will run when someone makes a withdrawal'''
        self.elixir-=Welixir
        self.withdraw+=Welixir
        self.temp=self.elixir
        self.wist=0
        while self.temp>=600:
            self.temp-=600
            self.wist+=1

def encrypt_bank():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Bank_Balance.txt",'rb') as f:
        balance=f.read()
    balanceE=KEY.encrypt(balance)
    with open("DataBase\DATABASE_Bank_Balance.txt",'wb') as f:
        f.write(balanceE)

def encrypt_GMA():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Guild_Member_Account.txt",'rb') as f:
        GMA=f.read()
    GMA_E=KEY.encrypt(GMA)
    with open("DataBase\DATABASE_Guild_Member_Account.txt",'wb') as f:
        f.write(GMA_E)

def encrypt_GWA():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'rb') as f:
        GWA=f.read()
    GWA_E=KEY.encrypt(GWA)
    with open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'wb') as f:
        f.write(GWA_E)

def decrypt_bank():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Bank_Balance.txt",'rb') as f:
        Rbalance=f.read()
    balanceD=KEY.decrypt(Rbalance)
    with open("DataBase\DATABASE_Bank_Balance.txt",'wb') as f:
        f.write(balanceD)

def decrypt_GMA():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Guild_Member_Account.txt",'rb') as f:
        RGMA=f.read()
    GMA_D=KEY.decrypt(RGMA)
    with open("DataBase\DATABASE_Guild_Member_Account.txt",'wb') as f:
        f.write(GMA_D)

def decrypt_GWA():
    KEY=KEYHOLDER.KEY
    with open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'rb') as f:
        RGWA=f.read()
    GWA_D=KEY.decrypt(RGWA)
    with open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'wb') as f:
        f.write(GWA_D)

def div():
    print("-----------------------------------")

data_objects=[]         #Objects Data
names=[]                #Names Data
elixir=[]               #Elixir Data
wists=[]                #Wists Data
withdrawn=[]            #Withdrawal Data

#Loading the Key
with open("key\key.txt",'rb') as f:
    k=f.read()
MAIN_KEY= Fernet(k)
KEYHOLDER.set_key(MAIN_KEY)

#############################################
## ONLY UPDATE BLACKLIST USER HERE NOTHING ELSE ##
BL=[5,6,7,9,10,11]
blacklist=sorted(BL)
#############################################
blacklistIndex=list(map(lambda x: x-1,blacklist))
ban="<:banned:1169524797567422495>"

decrypt_GMA()
#Collecting Database on Current Balance {Name/Elixir/Wists}
f=open("DataBase\DATABASE_Guild_Member_Account.txt",'r')
while True:
    l=f.readline()
    if not l:
        break
    names.append(   str(l.split(" ")[1])    )
    elixir.append(  int(l.split(" ")[2])    )
    wists.append(   int(l.split(" ")[3])    )
f.close()
encrypt_GMA()

decrypt_GWA()
#Collecting Database on Withdrawn Balance {Withdrawn Amount}
f=open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'r')
while True:
    l=f.readline()
    if not l:
        break
    withdrawn.append(   int(l.split(" ")[1]))
f.close
encrypt_GWA()

# Make Objects Based on {Guild members Count}
cM=len(names)
for i in range(0,cM):
    ob=guild(names[i],elixir[i],wists[i],withdrawn[i])
    data_objects.append(ob)

#Counting Guild Members
membercount=cM
#Counting Active Members
current_active_guild_members=membercount-len(blacklist)

div()
print("PPMINITY GUILD MANAGER")
div()
print("Hello, Hope you are doing well!")
div()
men=0
while men==0:
    print("What do you want to do?")
    print("1-> Credit Elixir")
    print("2-> Update Withdraw")
    print("3-> See Database")
    print("4-> Unlock Files ")
    print("5-> Exit")
    div()
    UI=int(input("Enter your input: "))
    div()
    match UI:
        case 1:
            
            decrypt_bank()
            decrypt_GMA()
            decrypt_GWA()
            #Getting Previous Elixir Balance
            with open("DataBase\DATABASE_Bank_Balance.txt",'r') as f:
                previous_elixir=int(f.read())

            #Getting Current Elixir
            current_elixir=int(input("Enter current Elixir: "))
            div()
            toAdd=(current_elixir-previous_elixir)//current_active_guild_members
            print(f"Everyone will receive {toAdd} elixir!")
            div()

            #Clearing Previously Stored Data
            names.clear()
            wists.clear()
            elixir.clear()
            withdrawn.clear()

            #Collecting Database on Current Balance {Name/Elixir/Wists}
            f=open("DataBase\DATABASE_Guild_Member_Account.txt",'r')
            while True:
                l=f.readline()
                if not l:
                    break
                names.append(   str(l.split(" ")[1])    )
                elixir.append(  int(l.split(" ")[2])    )
                wists.append(   int(l.split(" ")[3])    )
            f.close()

            #Collecting Database on Withdrawn Balance {Withdrawn Amount}
            f=open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'r')
            while True:
                l=f.readline()
                if not l:
                    break
                withdrawn.append(   int(l.split(" ")[1]))
            f.close

            for i in range(0,cM):
                data_objects[i].set_data(names[i],elixir[i],wists[i],withdrawn[i])

            #Crediting Elixir
            for index, i in enumerate(data_objects):
                if index in blacklistIndex :
                    i.BLelixir_update()
                    continue
                i.elixir_update(toAdd)

            #Updating Current Elixir As Previous Elixir in DATABASE_Bank_Balance.txt
            with open("DataBase\DATABASE_Bank_Balance.txt",'w') as f:
                f.write(str(current_elixir))

            #Updating database in DATABASE_Guild_Member_Account.txt
            with open("DataBase\DATABASE_Guild_Member_Account.txt",'w') as f:
                for i in range(membercount):
                    f.write(f"{i+1} {data_objects[i].name} {data_objects[i].elixir} {data_objects[i].wist}" + '\n')

            encrypt_bank()
            encrypt_GMA()
            encrypt_GWA()

            #Creating 0 ElixirUpdated Data Sheet.txt
            with open("Output\ElixirUpdate.txt",'w') as f:
                f.write(f"1• <@310672946316181514>  : {data_objects[0].elixir} <:elixir:1129376026036801636> | {data_objects[0].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"2• <@769243823649062934> : {data_objects[1].elixir} <:elixir:1129376026036801636> | {data_objects[1].wist} <:wist:1124833232454697040>\n\n") 
                f.write(f"3• <@490972376843157504>  : {data_objects[2].elixir} <:elixir:1129376026036801636> | {data_objects[2].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"4• <@746561159167082568> : {data_objects[3].elixir} <:elixir:1129376026036801636> | {data_objects[3].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"5• <@758223660653346847> : {data_objects[4].elixir} <:elixir:1129376026036801636> | {data_objects[4].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"6• <@822104471868932096>  : {data_objects[5].elixir} <:elixir:1129376026036801636> | {data_objects[5].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"7• <@780517300485750826>  : {data_objects[6].elixir} <:elixir:1129376026036801636> | {data_objects[6].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"8• <@907833128838631445>  : {data_objects[7].elixir} <:elixir:1129376026036801636> | {data_objects[7].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"9• <@1115587882145554473> : {data_objects[8].elixir} <:elixir:1129376026036801636> | {data_objects[8].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"10• <@723209891765944371> : {data_objects[9].elixir} <:elixir:1129376026036801636> | {data_objects[9].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"11• <@573893750468902912> : {data_objects[10].elixir} <:elixir:1129376026036801636> | {data_objects[10].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"12• <@1131012935767031859> : {data_objects[11].elixir} <:elixir:1129376026036801636> | {data_objects[11].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"13• <@1160465764340482178> : {data_objects[12].elixir} <:elixir:1129376026036801636> | {data_objects[12].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"14• <@1108864210970095717> : {data_objects[13].elixir} <:elixir:1129376026036801636> | {data_objects[13].wist} <:wist:1124833232454697040>\n\n")
                f.write("**Elixir Withdrawal Requirement**: 100+<:elixir:1129376026036801636>\n")
                f.write("**Wists Withdrawal Requirement**: 5+<:wist:1124833232454697040>") 
            print("Process is done")
            div()
        case 2:

            #Showing all the users
            for i in range(membercount):
                print(f"{i+1} • {data_objects[i].name} • {data_objects[i].elixir}")
            div()
            
            #Select the user who is withdrawing
            WUI=int(input("Who is making a withdrawal?: "))
            WUI=WUI-1
            div()
            print("You have choosen {}".format(data_objects[WUI].name))
            div()

            #Getting the amount of withdrawal & It can't exceed the balance
            while True:
                WA=int(input("Enter the amount to Withdraw: "))
                if WA<=data_objects[WUI].elixir:
                    break
                print(f"{data_objects[WUI].name} has only {data_objects[WUI].elixir}! So you cannot withdraw more than this!")

            #Updating that user's Account
            data_objects[WUI].elixir_withdraw(WA)

            decrypt_bank()
            decrypt_GMA()
            decrypt_GWA()

            #Reading Current Balance in DATABASE_Bank_Balance.txt
            with open("DataBase\DATABASE_Bank_Balance.txt",'r') as f:
                c_elixir=int(f.read())

            with open("DataBase\DATABASE_Bank_Balance.txt",'w') as f:
                f.write(str(c_elixir-WA))

            #Updating Data in DATABASE_Guild_Withdrawn_Account.txt
            with open("DataBase\DATABASE_Guild_Withdrawn_Account.txt",'w') as f:
                for i in range(membercount):
                    f.write(f"{i+1} {data_objects[i].withdraw}" + '\n')

            #Updating Data in Guild_Member_Account.txt
            with open("DataBase\DATABASE_Guild_Member_Account.txt",'w') as f:
                for i in range(membercount):
                    f.write(f"{i+1} {data_objects[i].name} {data_objects[i].elixir} {data_objects[i].wist} " + '\n')

            encrypt_bank()
            encrypt_GMA()
            encrypt_GWA()

            #Creating 1 ElixirWithdrawal Data Sheet.txt
            with open("Output\ElixirWithdraw.txt",'w') as f:
                f.write(f"1• <@310672946316181514>  : {data_objects[0].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"2• <@769243823649062934> : {data_objects[1].withdraw} <:elixir:1129376026036801636>\n\n") 
                f.write(f"3• <@490972376843157504>  : {data_objects[2].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"4• <@746561159167082568> : {data_objects[3].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"5• <@758223660653346847> : {data_objects[4].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"6• <@822104471868932096>  : {data_objects[5].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"7• <@780517300485750826>  : {data_objects[6].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"8• <@907833128838631445>  : {data_objects[7].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"9• <@1115587882145554473> : {data_objects[8].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"10• <@723209891765944371> : {data_objects[9].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"11• <@573893750468902912> : {data_objects[10].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"12• <@1131012935767031859> : {data_objects[11].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"13• <@1160465764340482178> : {data_objects[12].withdraw} <:elixir:1129376026036801636>\n\n")
                f.write(f"14• <@1108864210970095717> : {data_objects[13].withdraw} <:elixir:1129376026036801636>\n\n")

            #Creating 0 ElixirUpdated Data Sheet.txt
            with open("Output\ElixirUpdate.txt",'w') as f:
                f.write(f"1• <@310672946316181514>  : {data_objects[0].elixir} <:elixir:1129376026036801636> | {data_objects[0].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"2• <@769243823649062934> : {data_objects[1].elixir} <:elixir:1129376026036801636> | {data_objects[1].wist} <:wist:1124833232454697040>\n\n") 
                f.write(f"3• <@490972376843157504>  : {data_objects[2].elixir} <:elixir:1129376026036801636> | {data_objects[2].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"4• <@746561159167082568> : {data_objects[3].elixir} <:elixir:1129376026036801636> | {data_objects[3].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"5• <@758223660653346847> : {data_objects[4].elixir} <:elixir:1129376026036801636> | {data_objects[4].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"6• <@822104471868932096>  : {data_objects[5].elixir} <:elixir:1129376026036801636> | {data_objects[5].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"7• <@780517300485750826>  : {data_objects[6].elixir} <:elixir:1129376026036801636> | {data_objects[6].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"8• <@907833128838631445>  : {data_objects[7].elixir} <:elixir:1129376026036801636> | {data_objects[7].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"9• <@1115587882145554473> : {data_objects[8].elixir} <:elixir:1129376026036801636> | {data_objects[8].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"10• <@723209891765944371> : {data_objects[9].elixir} <:elixir:1129376026036801636> | {data_objects[9].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"11• <@573893750468902912> : {data_objects[10].elixir} <:elixir:1129376026036801636> | {data_objects[10].wist} <:wist:1124833232454697040> {ban}\n\n")
                f.write(f"12• <@1131012935767031859> : {data_objects[11].elixir} <:elixir:1129376026036801636> | {data_objects[11].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"13• <@1160465764340482178> : {data_objects[12].elixir} <:elixir:1129376026036801636> | {data_objects[12].wist} <:wist:1124833232454697040>\n\n")
                f.write(f"14• <@1108864210970095717> : {data_objects[13].elixir} <:elixir:1129376026036801636> | {data_objects[13].wist} <:wist:1124833232454697040>\n\n")
                f.write("**Elixir Withdrawal Requirement**: 100+<:elixir:1129376026036801636>\n")
                f.write("**Wists Withdrawal Requirement**: 5+<:wist:1124833232454697040>") 
            div()
            print("Process is done")
            div()
        case 3:
            for i in range(membercount):
                print(f"•Name• {data_objects[i].name}\n•Elixir• {data_objects[i].elixir}\n•Wists• {data_objects[i].wist}\n•Withdrawn Up Until Now• {data_objects[i].withdraw}\n\n")
            div()

            decrypt_bank()

            with open("DataBase\DATABASE_Bank_Balance.txt",'r') as f:
                c_elixir=int(f.read())
            print(f"Current Vault Balance• {c_elixir}")

            encrypt_bank()

            div()
        case 4:
            print("UNLOCKING FILES")
            div()
            decrypt_bank()
            decrypt_GMA()
            decrypt_GWA()
            print("DATABASE HAS BEEN UNLOCKED!")
            div()
            while (press := input("PRESS 0 WHEN YOU ARE DONE: ")) != "0":
                pass
            encrypt_bank()
            encrypt_GMA()
            encrypt_GWA()
            div()
            print("DATABASE HAS BEEN LOCKED!")
            div()
            print("EXITING, CHANGE DETECTED. PLEASE RESTART THE PROGRAM")
            div()
            break
        case 5:
            men=1
            break
        case _:
            div()
            print("Enter valid input")
            div()