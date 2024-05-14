from tkinter import *
window=Tk()
window.geometry("600x500")
window.title("CALCULATOR")
window.resizable(0,0)
def Action_button_click(item):
    global expression
    expression=expression+str(item)
    input_text.set(expression)

def Action_button_clear():
    global expression
    expression=""
    input_text.set("")

def Action_button_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""

expression = ""
input_text=StringVar()

input_frame = Frame(window, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)

input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 50)

button_frame = Frame(window, bg = "grey")
button_frame.pack()

Button_Clear = Button(button_frame, text = "CLEAR", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_clear())
Button_Clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

Button_Divide = Button(button_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_click("/"))
Button_Divide.grid(row = 0, column = 3, padx = 1, pady = 1)

Button_Seven = Button(button_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(7))
Button_Seven.grid(row = 1, column = 0, padx = 1, pady = 1)

Button_Eight = Button(button_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(8))
Button_Eight.grid(row = 1, column = 1, padx = 1, pady = 1)

Button_Nine = Button(button_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(9))
Button_Nine.grid(row = 1, column = 2, padx = 1, pady = 1)

Button_Multiply = Button(button_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_click("*"))
Button_Multiply.grid(row = 1, column = 3, padx = 1, pady = 1)

Button_Four = Button(button_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(4))
Button_Four.grid(row = 2, column = 0, padx = 1, pady = 1)

Button_Five = Button(button_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(5))
Button_Five.grid(row = 2, column = 1, padx = 1, pady = 1)

Button_Six = Button(button_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(6))
Button_Six.grid(row = 2, column = 2, padx = 1, pady = 1)

Button_Substract = Button(button_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_click("-"))
Button_Substract.grid(row = 2, column = 3, padx = 1, pady = 1)

Button_One = Button(button_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(1))
Button_One.grid(row = 3, column = 0, padx = 1, pady = 1)

Button_Two = Button(button_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(2))
Button_Two.grid(row = 3, column = 1, padx = 1, pady = 1)

Button_Three = Button(button_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(3))
Button_Three.grid(row = 3, column = 2, padx = 1, pady = 1)

Button_Add = Button(button_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_click("+"))
Button_Add.grid(row = 3, column = 3, padx = 1, pady = 1)

Button_Zero = Button(button_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: Action_button_click(0))
Button_Zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

Button_Point= Button(button_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_click("."))
Button_Point.grid(row = 4, column = 2, padx = 1, pady = 1)

Button_Equal_To = Button(button_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: Action_button_equal())
Button_Equal_To.grid(row = 4, column = 3, padx = 1, pady = 1)

window.mainloop()