from tkinter import *
root = Tk()
root.geometry('600x400')
root.title ('Телефонная  Книга')
root.config (bg = 'light grey')
root.resizable (0,0)


Database = [
    ['Drew', 'DeLeon', '4567891', 'address4', 'drew@deleon.com'],
    ]

FirstName = StringVar()
LastName = StringVar()
ContactNumber = StringVar()
Address = StringVar()
Email = StringVar()

frame = Frame(root)
frame.pack (side = RIGHT)

scroll = Scrollbar(frame, orient = VERTICAL)
select = Listbox (frame, yscrollcommand = scroll.set, height =15,)
scroll.config (command = select.yview)
scroll.pack(side = RIGHT, fill = Y)
select.pack(side = LEFT, fill = BOTH, expand = 1)

def selected():
    return int(select.curselection()[0])

def add():
    Database.append([FirstName.get(), LastName.get(),
                    ContactNumber.get(), Address.get(), Email.get()])
    print(f"Contact added.")

def delete():
    del Database[select()]

def selectset():
    #сделать руками без встроенного метода
    Database.sort()

def search():
    #сделать руками без встроенного метода
    Database.search()
    

Label(root, text = 'First Name', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=20)
Entry(root, textvariable = FirstName).place (x=130, y=20)
#Last name
#Contact Number
#Addres
#email
Label(root, text = 'Last Name', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=70)
Entry(root, textvariable = LastName).place (x=130, y=70)

Label(root, text = 'Contact Number', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=120)
Entry(root, textvariable = ContactNumber).place (x=130, y=120)

Label(root, text = 'Address', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=170)
Entry(root, textvariable = Address).place (x=130, y=170)

Label(root, text = 'Email', font = 'arial 12 bold', bg = 'white', fg='black') .place (x=30, y=220)
Entry(root, textvariable = Email).place (x=130, y=220)

Button(root, text = 'Add Contact', font = 'arial 12 bold', bg = 'white', command = add).place(x=70,y=280)
#Delete
#Search
#Sort contacts
#exit

root.mainloop()
