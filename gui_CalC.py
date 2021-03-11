from tkinter import *
root = Tk()

root.title("Simple Calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
e.insert(0,'0')
def button_click(number):
    current = e.get()

    if current == '+':

        e.delete(0, END)
        e.insert(0,str(number))
    elif current == '*':
        e.delete(0, END)
        e.insert(0, str(number))
    elif current == '-':
        e.delete(0, END)
        e.insert(0, str(number))
    elif current == '/':
        e.delete(0, END)
        e.insert(0, str(number))
    elif current=='0':
        e.delete(0, END)
        e.insert(0, str(number))
    else:
        e.delete(0, END)
        e.insert(0, str(current)+str(number))

def button_clr():
    e.delete(0, END)
    e.insert(0,'0')
def buttone_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)

    e.delete(0, END)
    e.insert(0, '+')
def buttone_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)

    e.delete(0, END)
    e.insert(0, '-')
def buttone_mul():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)

    e.delete(0, END)
    e.insert(0, '*')
def buttone_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)

    e.delete(0, END)
    e.insert(0, '/')

def button_eql():
    second_number = e.get()
    e.delete(0, END)
    global math
    try:
        if math=='addition':
            e.insert(0, f_num + float(second_number))
        elif math=="subtraction":
            e.insert(0, f_num - float(second_number))
        elif math=="division":
            e.insert(0, f_num / float(second_number))
        elif math=="multiplication":
            e.insert(0, f_num * float(second_number))
        elif math == 'null':
            e.insert(0, float(second_number))
        math = 'null'
    except:
        e.insert(0, float(second_number))





button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3)).grid(row=3, column=2)
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9)).grid(row=1, column=2)
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)

button_add = Button(root, text='+', padx=39, pady=20, command=buttone_add)
button_add.grid(row=5, column=0)
button_sub = Button(root, text='-', padx=41, pady=20, command=buttone_sub)
button_sub.grid(row=6, column=0)
button_div = Button(root, text='/', padx=40, pady=20, command=buttone_div)
button_div.grid(row=6, column=2)
button_mul = Button(root, text='x', padx=42, pady=20, command=buttone_mul)
button_mul.grid(row=6, column=1)


button_eq = Button(root, text='=', padx=91, pady=20, command=lambda: button_eql()).grid(row=5, column=1, columnspan=2)

button_clear = Button(root, text='CLEAR', padx=78, pady=20, command=button_clr).grid(row=4, column=1, columnspan=2)

root.mainloop()
