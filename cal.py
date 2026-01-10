import tkinter as tk
root=tk.Tk()
root.title("Calculator")
root.geometry("400x550")
root.resizable(False,False)
root.configure(bg="lightgrey")
entry1=tk.Entry(root,font=("bold",20),bg="black",fg="white",bd=0,justify="right")
entry1.grid(row=0,column=0,columnspan=4,padx=20,pady=20,ipady=10)
buttons=["7","8","9","/",
         "4","5","6","*",
         "1","2","3","-",
         "0",",","=","+"]
def press(v):
    entry1.insert(tk.END,v)
def clear():
    entry1.delete(0,tk.END)
def bksp():
    current=entry1.get()
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,current[:-1])
def cal():
    try:
        res=eval(entry1.get())
        entry1.delete(0,tk.END)
        entry1.insert(0,res)
    except:
        entry1.delete(0,tk.END)
        entry1.insert(0,"Error")
r=1
c=0
for i in buttons:
    cmd=cal if i=="=" else lambda x=i: press(x)
    tk.Button(root,font=("bold",20),command=cmd,text=i,bg="white" if i in "+-*/=" else "white",fg="black",bd=0,width=5,height=2).grid(row=r,column=c,columnspan=1,padx=2,pady=2)
    c+=1
    if c==4:
        c=0
        r+=1
tk.Button(root,font=("bold",20),text="CLEAR",command=clear,bg="white",fg="black",bd=0,width=6,height=2).grid(row=r,column=0,columnspan=1,padx=6,pady=6)
tk.Button(root,font=("bold",20),text="BKSP",command=bksp,bg="white",fg="black",bd=0,width=6,height=2).grid(row=r,column=2,columnspan=1,padx=6,pady=6)
root.mainloop()
