from tkinter import * 
from tkinter import font as tkFont
import parser

root=Tk()

root.title("Calculator")

fonts = tkFont.Font(family='Helvetica', size=14, weight=tkFont.BOLD)

#adding the input field
display=Entry(root,bg="Silver",font=fonts)
display.grid(row=1,columnspan=6,sticky=W+E,ipady=18)

#adding buttons to the Calculator

Button(root,text="1", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_variables(1)).grid(row=2,column=0)
Button(root,text="2", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_variables(2)).grid(row=2,column=1)
Button(root,text="3", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_variables(3)).grid(row=2,column=2)

Button(root,text="4", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3,command=lambda :get_variables(4)).grid(row=3,column=0)
Button(root,text="5", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3,command=lambda :get_variables(5)).grid(row=3,column=1)
Button(root,text="6", activebackground="Blue", bg="Pink",font=fonts, width=10,height=3,command=lambda :get_variables(6)).grid(row=3,column=2)

Button(root,text="7", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3,command=lambda :get_variables(7)).grid(row=4,column=0)
Button(root,text="8", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3,command=lambda :get_variables(8)).grid(row=4,column=1)
Button(root,text="9", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3,command=lambda :get_variables(9)).grid(row=4,column=2)

#adding other buttons
Button(root,text="AC", activebackground="Blue", bg="Red",fg="White",  font=fonts, width=10,height=3,command=lambda :clear_all()).grid(row=5,column=0)
Button(root,text="0", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3,command=lambda :get_variables(0)).grid(row=5,column=1)
Button(root,text="=", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3, command=lambda:calculate()).grid(row=5,column=2)

Button(root,text="+", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3, command=lambda :get_operation("+")).grid(row=2,column=3)
Button(root,text="-", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_operation("-")).grid(row=3,column=3)
Button(root,text="*", activebackground="Blue", bg="Pink", font=fonts,  width=10,height=3,command=lambda :get_operation("*")).grid(row=4,column=3)
Button(root,text="/", activebackground="Blue", bg="Pink", font=fonts,  width=10,height=3,command=lambda :get_operation("/")).grid(row=5,column=3)

#adding new operations
Button(root,text="pi", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3, command=lambda :get_operation("*3.14")).grid(row=2,column=4)
Button(root,text="%", activebackground="Blue", bg="Pink",font=fonts,   width=10,height=3,command=lambda :get_operation("%")).grid(row=3,column=4)
Button(root,text="(", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_operation("(")).grid(row=4,column=4)
Button(root,text="exp", activebackground="Blue", bg="Pink",font=fonts,   width=10,height=3,command=lambda :get_operation("**")).grid(row=5,column=4)

Button(root,text="DEL", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3,command=lambda :undo()).grid(row=2,column=5)
Button(root,text=".", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3,command=lambda :get_operation(".") ).grid(row=3,column=5)
Button(root,text=")", activebackground="Blue", bg="Pink", font=fonts, width=10,height=3, command=lambda :get_operation(")")).grid(row=4,column=5)
Button(root,text="^2", activebackground="Blue", bg="Pink",font=fonts,  width=10,height=3, command=lambda :get_operation("**2")).grid(row=5,column=5)

#get the user input and place it in the text field
i=0
def get_variables(num):
    global i 
    display.insert(i,num)
    i+=1  

#clearing all
def clear_all():
    display.delete(0,END)

#deleting single element
def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

#getting operations
def get_operation(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

#calculationg result
def calculate():
    entire_string=display.get()
    try:
        a = parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")


root.mainloop()