import tkinter as tk
from tkinter import *

# --- Window Setup ---
root = Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="black")

# --- Optional icon (make sure 'calculatoricon.ico' exists in same folder) ---
try:
    icon_image = PhotoImage(file="calculatoricon.ico")
    root.iconphoto(False, icon_image)
except Exception:
    pass  # skip if icon file not found

# --- Global Equation Variable ---
equation = ""

# --- Functions ---
def show(value):
    global equation
    equation += str(value)
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    if equation != "":
        try:
            result = eval(equation)
            label_result.config(text=result)
            equation = str(result)
        except Exception:
            label_result.config(text="Error")
            equation = ""

# --- Display Label ---
label_result = Label(
    root,
    width=25,
    height=2,
    text="",
    font=("arial", 30, "bold"),
    fg="white",
    bg="black",
    anchor="e"
)
label_result.pack(pady=10)

# --- Button Function Helper ---
def create_button(text, x, y, color="#2a2d36", w=5, h=1, cmd=None):
    Button(
        root,
        text=text,
        width=w,
        height=h,
        font=("arial", 30, "bold"),
        bd=1,
        fg="#fff",
        bg=color,
        command=cmd
    ).place(x=x, y=y)

# --- Buttons ---
create_button("C", 10, 100, "#3697f5", cmd=clear)
create_button("/", 150, 100, cmd=lambda: show("/"))
create_button("%", 290, 100, cmd=lambda: show("%"))
create_button("*", 430, 100, cmd=lambda: show("*"))

create_button("7", 10, 200, cmd=lambda: show("7"))
create_button("8", 150, 200, cmd=lambda: show("8"))
create_button("9", 290, 200, cmd=lambda: show("9"))
create_button("-", 430, 200, cmd=lambda: show("-"))

create_button("4", 10, 300, cmd=lambda: show("4"))
create_button("5", 150, 300, cmd=lambda: show("5"))
create_button("6", 290, 300, cmd=lambda: show("6"))
create_button("+", 430, 300, cmd=lambda: show("+"))

create_button("1", 10, 400, cmd=lambda: show("1"))
create_button("2", 150, 400, cmd=lambda: show("2"))
create_button("3", 290, 400, cmd=lambda: show("3"))

# 0 is double-width
create_button("0", 10, 500, w=11, cmd=lambda: show("0"))
create_button(".", 290, 500, cmd=lambda: show("."))

# = is tall
Button(
    root,
    text="=",
    width=5,
    height=3,
    font=("arial", 30, "bold"),
    bd=1,
    fg="#fff",
    bg="#fe9037",
    command=calculate
).place(x=430, y=400)

# --- Run the App ---
root.mainloop()
