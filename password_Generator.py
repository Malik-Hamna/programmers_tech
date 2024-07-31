import random 
import string
from tkinter import *
import tkinter as tk
from tkinter import messagebox


root=tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#DCD9D8")

def generate():
     num=int(e1.get())
     s1=string.ascii_lowercase
     s2=string.ascii_uppercase
     s3=string.punctuation
     s4=string.digits

     s=[]
     s.extend(list(s1))
     s.extend(list(s2))
     s.extend(list(s3))
     s.extend(list(s4))

     random.shuffle(s)
     password = ''.join(s[:num])  # Convert list to string 

     
     L4=Label(root,text="Password  " , font =("Cursive", 12) ,bg="#765385", fg="white")
     L4.place(x=25, y=200)
     #created password show here
     L5=Label(root,text= password , font =("Cursive", 12) ,bd=2,bg="white", fg="black")
     L5.place(x=120, y=250)

     copy_button = Button(root, text="Copy Password", fg="black", bg="#DCD9D8", font=("Serif", 13), command=lambda: copy(password))
     copy_button.place(x=120, y=300)

def copy(password):
     root.clipboard_clear()
     root.clipboard_append(password)
     root.update()  # Keeps the clipboard content after the window is closed
     messagebox.showinfo("Copied", "Password copied to clipboard!")


L1=Label(root,text="Password Generator app" , font =("Cursive", 12) ,bg="#765385", fg="white")
L1.place(x=120, y=30)
L2=Label(root,text="Enter Password Length:" , font =("Arial", 10,"bold" ,"italic") ,bg="#DCD9D8", fg="black")
L2.place(x=20, y=90)


 
e1=Entry(root, width=20, bd=2, font="Cursive" ) 
e1.place(x=120, y=110)

Generate_button=Button(root, text="Generate Password", fg="black", bg="#DCD9D8", font=("Serif",13),command=generate)
Generate_button.place(x=120,y=160)






root.mainloop()