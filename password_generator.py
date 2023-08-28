from tkinter import *
from tkinter import messagebox 
from random import randint,choice,shuffle
import random, string


all_combi = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

def password_generator():
    password = ""
    for y in range(pass_len.get()):
        char_type = random.choice(all_combi)   #to randomize the occurance of alphabet, digit or symbol
        password = password + random.choice(char_type)
     
    output_pass.set(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    name = input_user_name.get()
    length = input_pass_head.get()
    
    name_password = output_pass.get()

    with open('password.txt','w') as data:
        if len(name)==0 or len(name_password)==0 and len(length)==0:  
            option = messagebox.showinfo(title="Uhh-ohh", message="Oops missed a field")
        else:
            option = messagebox.askokcancel(title="Confirm",
                                            message=f"Your Name: {name} \nLength: {length} \nPassword: {name_password}\nSave?")  
            if option:
                data.write(f"{name} || {length} || {name_password}\n")   
                option = messagebox.showinfo(title="Success", message="Successfully Saved")
                input_password.delete(0, END)
                input_user_name.delete(0, END)
                
            
            data.close()

                  

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Generator")
window.geometry("600x540+0+0")
window.config(bg='white',padx=50, pady=50)
output_pass = StringVar()


# ------------------------------------------
user_name_label= Label(width=10,text="User Name:",font = 'arial 12 bold')
user_name_label.config(bg="white")
user_name_label.grid(row=0,column=0,padx=10,sticky=W)

input_user_name=Entry(width=40)
input_user_name.grid(row=0,column=1,padx=10,pady=10,sticky=W,columnspan=2)     
input_user_name.focus()   #Puts cursor in textbox.

pass_head = Label( text = 'Password Length', font = 'arial 12 bold')#to generate label heading 
pass_head.config(bg="white")
pass_head.grid(row=2,column=0,padx=10,sticky=W)

input_pass_head=Entry(width=40)
pass_len = IntVar() #integer variable to store the input of length of the password wanted
length = Spinbox(textvariable = pass_len , from_ = 0, to = 32 ,width = 24, font='arial 16')
length.grid(row=2,column=1,padx=10,pady=50,sticky=W,columnspan=2) 
input_pass_head.grid(row=2,column=1,padx=10,pady=50,sticky=W,columnspan=2)     


password_label= Label(text="Password:",font = 'arial 12 bold')
password_label.config(bg="white")
password_label.grid(row=3,column=0,padx=10,sticky=W)

input_password=Entry(window, width=25, textvariable=output_pass)
input_password.grid(row=3,column=1,padx=10,pady=10,sticky=W)

password_button=Button(text='Generate Password',command=password_generator)
password_button.grid(row=5,column=1,columnspan=2,padx=10,pady=15,sticky=W)

add_button=Button(text='Accept',width=25,command=save_data)
add_button.grid(row=6,column=1,columnspan=2,padx=10,pady=8,sticky=W)


window.mainloop()
