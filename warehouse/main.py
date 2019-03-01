dic = [['Lee',123,4560,'Clothes'],['Parle',90,56,'Biscuit'],['SD-Card',8,890,'Computer'],['oreo',890,78,'Biscuit'],['LOR',8,550,'Books'],['Milton',56,600,'Bottles'],['Nike',5000,4000,'shoes']]
from tkinter import *
root=Tk()
root.geometry("312x324")
root.resizable(0, 0)
root.title("Warehouse")
s =""
top=Toplevel()
l1=Label(top)
l1.pack()
def press():
    arr = sorted(dic,key=lambda dic:dic[1])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="  "+str(arr[i][j])+"         "
        ans+='\n'
    print(ans)
    l1.config(text=ans)
#defining second event
def press1():
    arr = sorted(dic,key=lambda dic:dic[2])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

#defining third event
def press2():
    arr = sorted(dic,key=lambda dic:dic[3])
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

#defining fourth event

def press3():
    arr = sorted(dic,key=lambda dic:dic[1],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="  "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press4():
    arr = sorted(dic,key=lambda dic:dic[2],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="     "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)

def press5():
    arr = sorted(dic,key=lambda dic:dic[3],reverse=True)
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)


def pressno():
    arr = dic
    ans = ' Name       Quant.  Price       Category \n'
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ans+="        "+str(arr[i][j])+"       "
        ans+='\n'
    print(ans)
    l1.config(text=ans)
def open_window():
    top=Toplevel()

    top.title("new window")
    top.geometry("402x324")
    button4=Button(top,text="close",fg="green",command=top.destroy)
    button4.pack(side=LEFT)
    button1 = Button(top, text="View Data", fg="red", command=pressno)
    button1.pack(side=LEFT)

    button2 = Button(top, text="Quantity", fg="red", command=press)
    button2.pack(side=LEFT)

    button3 =Button(top, text="Price", fg="red", command=press1)
    button3.pack(side=LEFT)

    button4 = Button(top, text="Category", fg="red", command=press2)
    button4.pack(side=LEFT)

    button5 = Button(top, text="Quantity DSC", fg="red", command=press3)
    button5.pack(side=LEFT)

    button6 = Button(top, text="Price DSC", fg="red", command=press4)
    button6.pack(side=LEFT)




def password():

    s=entry.get()
    if(s=="jo_bhi_rakh_lo"):



        button3 = Button(root, text="click here to know your options", command=open_window,fg="green",bg="pink")
        button3.pack(side=LEFT)
        button = Button(root, text="Quit", fg="red", bg="pink" ,command=quit)
        button.pack(side=LEFT)




entry=Entry(root)
entry.pack()
button=Button(root,text="enter password ",command=password)
button.pack()


root.mainloop()
