import tkinter as tk

calculation = ""
def add_to_calculate(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)
def evaluate_calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root = tk.Tk()
root.title("GUI Calculator")
root.geometry("320x300")
root.resizable(False, False)
root.configure(bg='black')

  # Set the main window background color to black

# Creating and configuring the text widget
text_result = tk.Text(
    root,
    height=1,
    width=15,
    font=("Arial", 25),
    bg='black',
    fg='white',
    padx=10,  # internal padding along x-axis
    pady=10,  # internal padding along y-axis
    bd=1,     # border width
    relief='ridge',  # border style
    highlightthickness=2,  # highlight border thickness
    highlightbackground='grey',  # highlight border color
    highlightcolor="black"
)
text_result.grid(columnspan=6, padx=10)  # External padding on left and right


# Define button colors
number_bg = "#E0E0E0"
number_fg = "#000000"
operator_bg = "#FF5733"
operator_fg = "#FFFFFF"
special_bg = "#33FF57"
special_fg = "#FFFFFF"
equal_bg = "#A020F0"
equal_fg = "#FFFFFF"


button_config = {
    'width': 5,
    'font': ("Arial", 15),
    'bd': 0,  # Border width
    'highlightthickness': 0,  # Highlight thickness
    'fg': "#32036b",
    'bg': "#fff"
}


btn_1=tk.Button(root, text="1", command=lambda: add_to_calculate(1),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_1.grid(column=1, row=2,pady=5)
btn_2=tk.Button(root, text="2", command=lambda: add_to_calculate(2),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_2.grid(column=2, row=2,pady=5)
btn_3=tk.Button(root, text="3", command=lambda: add_to_calculate(3),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_3.grid(column=3, row=2,pady=5)
btn_4=tk.Button(root, text="4", command=lambda: add_to_calculate(4),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_4.grid(column=1, row=3,pady=5)
btn_5=tk.Button(root, text="5", command=lambda: add_to_calculate(5),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_5.grid(column=2, row=3,pady=5)
btn_6=tk.Button(root, text="6", command=lambda: add_to_calculate(6),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_6.grid(column=3, row=3,pady=5)
btn_7=tk.Button(root, text="7", command=lambda: add_to_calculate(7),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_7.grid(column=1, row=4,pady=5)
btn_8=tk.Button(root, text="8", command=lambda: add_to_calculate(8),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_8.grid(column=2, row=4,pady=5)
btn_9=tk.Button(root, text="9", command=lambda: add_to_calculate(9),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_9.grid(column=3, row=4,pady=5)
btn_0=tk.Button(root, text="0", command=lambda: add_to_calculate(0),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_0.grid(column=2, row=5,pady=5)
btn_plus=tk.Button(root, text="+", command=lambda: add_to_calculate("+"),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_plus.grid(column=4, row=2,pady=5)
btn_minus=tk.Button(root, text="-", command=lambda: add_to_calculate("-"),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_minus.grid(column=4, row=3,pady=5)
btn_mul=tk.Button(root, text="*", command=lambda: add_to_calculate("*"),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_mul.grid(column=4, row=4,pady=5)
btn_division=tk.Button(root, text="/", command=lambda: add_to_calculate("/"),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_division.grid(column=4, row=5,pady=5)
btn_open=tk.Button(root, text="(", command=lambda: add_to_calculate("("),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_open.grid(column=1, row=5,pady=5)
btn_close=tk.Button(root, text=")", command=lambda: add_to_calculate(")"),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_close.grid(column=3, row=5,pady=5)
btn_clear=tk.Button(root, text="C", command=clear_field,width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#e68a00" )
btn_clear.grid(column=1, row=6,pady=5)
btn_point=tk.Button(root, text=".", command=lambda: add_to_calculate("."),width=5,font=("Arial", 15),bd=1,fg="#32036b", bg="#fff" )
btn_point.grid(column=2, row=6,pady=5)
btn_equal=tk.Button(root, text="=", command=evaluate_calculate,width=11,font=("Arial", 15),bd=1,fg="#32036b", bg="#ffebcc" )
btn_equal.grid(column=3, row=6,columnspan=2,pady=5)


root.mainloop()

