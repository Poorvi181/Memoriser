from tkinter import*
from tkinter.filedialog import*

root=Tk()
root.title("Memoriser")

def openfile():
    a=askopenfile(title="openfile")
    if a is not None:
        listbox.delete(0,END)
        items=a.readlines()
        for item in items:
            listbox.insert(END,item.strip())

def savefile():
    b=asksaveasfile(defaultextension=".txt")
    if b is not None:
        for item in listbox.get(0,END):
            print(item.strip(),file=b)
        listbox.delete(0,END)
openbutton=Button(root,text="Open",width=15,command=openfile)
openbutton.pack(side=LEFT)

deletebutton=Button(root,text="Delete",width=15)
deletebutton.pack(side=RIGHT)

savebutton=Button(root,text="Save",width=15,command=savefile)
savebutton.pack(padx=5,pady=5)

entrybox=Entry(root,width=30)
entrybox.pack(padx=5,pady=5)

addbutton=Button(root,text="Add",width=15)
addbutton.pack(padx=5,pady=5)

frame=Frame(root)
frame.pack()

scrollbar=Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(frame,width=70,bg="red",yscrollcommand=scrollbar.set)
for i in range(50,151):
    listbox.insert(END,"Poorvi"+str(i))
listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)
root.mainloop()