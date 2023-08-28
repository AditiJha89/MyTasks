from tkinter import *
import math
import tkinter.messagebox
 
root = Tk()
root.configure(background = 'white')
root.resizable(0,0)
root.geometry("340x300+450+140")
root.title("Calculator")
equa = Frame(root)
equa.grid()
 
class Calculation():
    def __init__(self):
        self.total=0
        self.current=''
        self.input_value=True
        self.check_sum=False
        self.op=''
        self.result=False
 
    def enterVal(self, num):
        self.result=False
        firstnum=txtDisplay.get()
        secondnum=str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value=False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum+secondnum
        self.display(self.current)
 
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtDisplay.get())
 
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
 
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value=True
        self.check_sum=False
        self.display(self.total)
 
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input_value=True
        self.check_sum=True
        self.op=op
        self.result=False
 
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value=True
        
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)
        
    def math(self):
         self.result = False
         self.current = -(float(txtDisplay.get()))
         self.display(self.current)
 
    def squared(self):
         self.result = False
         self.current = math.sqrt(float(txtDisplay.get()))
         self.display(self.current)
         
         
value = Calculation()
 
txtDisplay = Entry(equa, font=('times new roman',20,'bold'),bg='white',fg='black',bd=5,width=23,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")
 
number = "789456123"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(equa, width=3, height=1,bg='white',fg='black',font=('times new roman',10,'bold'),bd=4,text=number[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=number[i]:value.enterVal(x)
        i+=1
       
clear_button = Button(equa, text=chr(67),width=3,height=1,bg='white',font=('times new roman',10,'bold')
                  ,bd=4, command=value.Clear_Entry
                 ).grid(row=1, column= 0, pady = 1)
 
btnsq = Button(equa, text="\u221A",width=3, height=1,bg='white', font=('times new roman',10,'bold'),
               bd=4,command=value.squared
              ).grid(row=1, column= 1, pady = 1)

div_button = Button(equa, text="/",width=3,height=1,bg='white',font=('times new roman',10,'bold'),
                bd=4,command=lambda:value.operation("divide")
                ).grid(row=1, column= 2, pady = 1)

mod_button = Button(equa, text="%",width=3,
				height=1,bg='white',
				font=('times new roman',10,'bold'),
				bd=4,command=lambda:value.operation("mod")
				).grid(row=1, column= 3, pady = 1)

mul_button = Button(equa, text="x",width=3,height=1,bg='white',font=('times new roman',10,'bold'),
                bd=4,command=lambda:value.operation("multi")
                ).grid(row=2, column= 3, pady = 1)

sub_button = Button(equa, text="-",width=3,height=1,bg='white',font=('times new roman',10,'bold'),
                bd=4,command=lambda:value.operation("sub")
                ).grid(row=3, column= 3, pady = 1)
 
add_buttom = Button(equa, text="+",width=3, height=1,bg='white',font=('times new roman',10,'bold'),
                bd=4,command=lambda:value.operation("add")
                ).grid(row=4, column= 3, pady = 1)

equal_button = Button(equa, text="=",width=3,height=1,bg='white',font=('times new roman',10,'bold'),bd=4,
                   command=value.sum_of_total).grid(row=5, column= 3, pady = 1)

dot_button = Button(equa, text=".",width=3,height=1,bg='white',font=('times new roman',10,'bold'),
                bd=4,command=lambda:value.enterVal(".")
                ).grid(row=5, column= 2, pady = 1)


btnZero = Button(equa, text="0",width=3,height=1,bg='white',fg='black',font=('times new roman',10,'bold'),
                 bd=4,command=lambda:value.enterVal(0)
                 ).grid(row=5, column= 1, pady = 1)

btnPi = Button(equa, text="π",width=3,
			height=1,bg='white',fg='black',
			font=('times new roman',10,'bold'),
			bd=4,command=value.pi
			).grid(row=5, column= 0, pady = 1)
 
 
lblDisplay = Label(equa, text = "Calculation",            
                   font=('times new roman',20,'bold'),
                   bg='black',fg='white',justify=CENTER)
 
 
root.mainloop()