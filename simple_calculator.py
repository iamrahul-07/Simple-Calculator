from tkinter import * 
import math


#CREATING MAIN WINDOW
root=Tk()
root.geometry("500x630")
root.resizable(False,False)
root.title("SIMPLE CALCULATOR")
var=StringVar()      #Constructing string variable

#CREATING ENTRY FIELD

entry=Entry(root,font=("calibre 40"),bg="lightgrey",borderwidth=8,relief=SUNKEN,text=var)
entry.place(x=10,y=10,height=70,width=480)

#CREATING FUNCTION


#Function to show the entered value in the entry widget
def show(value):
    var.set(var.get()+value)


#Function to clear the entry widget
def clear():
    var.set("")


#Function to calculate any equations
def calculate(result):
    if entry.get() == "":
        var.set("Error")
    else:
        num = entry.get()
        try:
            result = eval(num)
            var.set(result)
        except:
            var.set("Error")


#Function to find factorial of any number 
def fact():
    if entry.get()=="":
        var.set("Error")
    else:
        num=int(entry.get())
        try:
            res=math.factorial(num)
            var.set(res)
        except:
            var.set("Invalid Input")


#Function to find square root of any number
def sqrt():
    if entry.get()=="":
        var.set("Error")
    else:
        num=float(entry.get())
        try:
            res=math.sqrt(num)
            var.set(res)
        except:
            var.set("Invalid Input")


#Function to find square of any number
def square():
    if entry.get()=="":
        var.set("Error")
    else:
        num=float(entry.get())
        try:
         res=num**2
         var.set(res)
        except:
            var.set("Invalid Input")


#CREATING SPECIAL BUTTONS


clear=Button(root,text="C",font=("calibre 20"),bg="orange",borderwidth=5,relief=RAISED,command=clear)
clear.place(x=20,y=100,height=70,width=70)

sqrt=Button(root,text="√",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=sqrt)
sqrt.place(x=150,y=100,height=70,width=70)

pi=Button(root,text="π",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("3.14159265358979"))
pi.place(x=280,y=100,height=70,width=70)

square=Button(root,text="x²",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=square)
square.place(x=410,y=100,height=70,width=70)

fact=Button(root,text="!",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=fact)
fact.place(x=20,y=460,height=70,width=70)

point=Button(root,text=".",font=("calibre 40"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("."))
point.place(x=280,y=460,height=70,width=70)

equal=Button(root,text="=",font=("calibre 30"),bg="orange",borderwidth=5,relief=RAISED,command=lambda : calculate("="))
equal.place(x=20,y=550,height=70,width=460)


#CREATING NUMBER BUTTONS

button0=Button(root,text="0",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("0"))
button0.place(x=150,y=460,height=70,width=70)

button1=Button(root,text="1",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("1"))
button1.place(x=20,y=370,height=70,width=70)

button2=Button(root,text="2",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("2"))
button2.place(x=150,y=370,height=70,width=70)

button3=Button(root,text="3",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("3"))
button3.place(x=280,y=370,height=70,width=70)

button4=Button(root,text="4",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("4"))
button4.place(x=20,y=280,height=70,width=70)

button5=Button(root,text="5",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("5"))
button5.place(x=150,y=280,height=70,width=70)

button6=Button(root,text="6",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("6"))
button6.place(x=280,y=280,height=70,width=70)

button7=Button(root,text="7",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("7"))
button7.place(x=20,y=190,height=70,width=70)

button8=Button(root,text="8",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("8"))
button8.place(x=150,y=190,height=70,width=70)

button9=Button(root,text="9",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("9"))
button9.place(x=280,y=190,height=70,width=70)


#CREATING ARITHMETIC BUTTON


#Button for adding the numbers
add=Button(root,text="+",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("+"))
add.place(x=410,y=190,height=70,width=70)

#Button for subtracting the numbers
sub=Button(root,text="-",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("-"))
sub.place(x=410,y=280,height=70,width=70)

#Button for multiplying the numbers
mul=Button(root,text="x",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("*"))
mul.place(x=410,y=370,height=70,width=70)

#Button for dividing the numbers
divide=Button(root,text="/",font=("calibre 20"),bg="skyblue",borderwidth=5,relief=RAISED,command=lambda : show("/"))
divide.place(x=410,y=460,height=70,width=70)

root.mainloop()