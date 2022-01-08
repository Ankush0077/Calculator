from tkinter import *

root = Tk()
root.title("Simple Calculator")

myEntry = Entry(root, width=35, borderwidth = 5)
myEntry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

def ButtonClick(Number):
    current = myEntry.get()
    myClickClear()
    myEntry.insert(0, str(current) + str(Number))
    
def myClickplus():
    number1 = myEntry.get()
    global int_num1
    int_num1 = int(number1)
    myClickClear()
    
def myClickClear():
    myEntry.delete(0, END)
  
def myClickequal():
    number2 = myEntry.get()
    myClickClear()
    myEntry.insert(0, int_num1 + int(number2))
    
myButton0 = Button(root, text = "0", command = lambda: ButtonClick(0), padx= 40, pady = 20)
myButton0.grid(row = 4, column = 0)

myButton1 = Button(root, text = "1", command = lambda: ButtonClick(1), padx= 40, pady = 20)
myButton1.grid(row = 3, column = 0)

myButton2 = Button(root, text = "2", command = lambda: ButtonClick(2), padx= 40, pady = 20)
myButton2.grid(row = 3, column = 1)

myButton3 = Button(root, text = "3", command = lambda: ButtonClick(3), padx= 40, pady = 20)
myButton3.grid(row = 3, column = 2)

myButton4 = Button(root, text = "4", command = lambda: ButtonClick(4), padx= 40, pady = 20)
myButton4.grid(row = 2, column = 0)

myButton5 = Button(root, text = "5", command = lambda: ButtonClick(5), padx= 40, pady = 20)
myButton5.grid(row = 2, column = 1)

myButton6 = Button(root, text = "6", command = lambda: ButtonClick(6), padx= 40, pady = 20)
myButton6.grid(row = 2, column = 2)

myButton7 = Button(root, text = "7", command = lambda: ButtonClick(7), padx= 40, pady = 20)
myButton7.grid(row = 1, column = 0)

myButton8 = Button(root, text = "8", command = lambda: ButtonClick(8), padx= 40, pady = 20)
myButton8.grid(row = 1, column = 1)

myButton9 = Button(root, text = "9", command = lambda: ButtonClick(9), padx= 40, pady = 20)
myButton9.grid(row = 1, column = 2)

myButtonplus = Button(root, text = "+", command = myClickplus, padx = 40, pady = 20)
myButtonplus.grid(row = 5, column = 0)

myButtonequal = Button(root, text = "=", command = myClickequal, padx = 90, pady = 20)
myButtonequal.grid(row = 5, column = 1, columnspan = 2)

myButtonClear = Button(root, text = "Clear", command = myClickClear, padx = 80, pady = 20)
myButtonClear.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()