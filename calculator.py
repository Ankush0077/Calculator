from tkinter import *
import keyboard

root = Tk()
root.title("Simple Calculator")


myEntry = Entry(root, width=35, borderwidth = 5)
myEntry.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)



def myClick1():
    keyboard.press_and_release('1')
    
def myClick2():
   keyboard.press_and_release('2')

def myClick3():
    keyboard.press_and_release('3')

def myClick4():
    keyboard.press_and_release('4')

def myClick5():
    keyboard.press_and_release('5')
   
def myClick6():
    keyboard.press_and_release('6')
    
def myClick7():
    keyboard.press_and_release('7')
    
def myClick8():
    keyboard.press_and_release('8')
    
def myClick9():
    keyboard.press_and_release('9')
    
def myClick0():
    keyboard.press_and_release('0')
    
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
    
    
myButton0 = Button(root, text = "0", command = myClick0, padx= 40, pady = 20)
myButton0.grid(row = 4, column = 0)

myButton1 = Button(root, text = "1", command = myClick1, padx= 40, pady = 20)
myButton1.grid(row = 3, column = 0)

myButton2 = Button(root, text = "2", command = myClick2, padx= 40, pady = 20)
myButton2.grid(row = 3, column = 1)

myButton3 = Button(root, text = "3", command = myClick3, padx= 40, pady = 20)
myButton3.grid(row = 3, column = 2)

myButton4 = Button(root, text = "4", command = myClick4, padx= 40, pady = 20)
myButton4.grid(row = 2, column = 0)

myButton5 = Button(root, text = "5", command = myClick5, padx= 40, pady = 20)
myButton5.grid(row = 2, column = 1)

myButton6 = Button(root, text = "6", command = myClick6, padx= 40, pady = 20)
myButton6.grid(row = 2, column = 2)

myButton7 = Button(root, text = "7", command = myClick7, padx= 40, pady = 20)
myButton7.grid(row = 1, column = 0)

myButton8 = Button(root, text = "8", command = myClick8, padx= 40, pady = 20)
myButton8.grid(row = 1, column = 1)

myButton9 = Button(root, text = "9", command = myClick9, padx= 40, pady = 20)
myButton9.grid(row = 1, column = 2)

myButtonplus = Button(root, text = "+", command = myClickplus, padx = 40, pady = 20)
myButtonplus.grid(row = 5, column = 0)

myButtonequal = Button(root, text = "=", command = myClickequal, padx = 90, pady = 20)
myButtonequal.grid(row = 5, column = 1, columnspan = 2)

myButtonClear = Button(root, text = "Clear", command = myClickClear, padx = 80, pady = 20)
myButtonClear.grid(row = 4, column = 1, columnspan = 2)

root.mainloop()