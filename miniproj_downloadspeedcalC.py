from tkinter import *
from tkinter import messagebox as mb

root = Tk()
root.resizable(False, False)
root.title("Internet speed calculator")
root.geometry('500x100')

lab1 = Label(root, text='Speed in Mbps(the real speed):').grid(row=0, column=0)
ntry1 = Entry(root)
ntry1.grid(row=0, column=2)


lab2 = Label(root, text='File size in GB:').grid(row=1, column=0)
ntry2 = Entry(root)
ntry2.grid(row=1, column=2)

def myclick():
    try:
        a= float(ntry1.get())
        b = float(ntry2.get())
        c =  (b*1000)/a
        d = str(c/60) + ' Minutes! or \n' + str(c/60/60) + 'Hours! to be exact'
        show = mb.showinfo('Answer', d)
    except:
        err = mb.showerror('ERROR!', 'Please write a number in the given field')



but = Button(root, text='Find!',width =1, padx=50, borderwidth=0.5, bg='#FFD700',fg ='blue', command=myclick).grid(row=3,column=1)


root.mainloop()
